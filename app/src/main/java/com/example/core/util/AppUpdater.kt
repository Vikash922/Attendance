package com.example.core.util

import android.app.DownloadManager
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.net.Uri
import android.os.Build
import android.os.Environment
import android.util.Log
import android.widget.Toast
import androidx.core.content.FileProvider
import com.example.BuildConfig
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONObject
import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL

data class UpdateInfo(
    val hasUpdate: Boolean,
    val latestVersionCode: Int,
    val latestVersionName: String,
    val apkUrl: String,
    val releaseNotes: String
)

object AppUpdater {
    private const val UPDATE_JSON_URL = "https://raw.githubusercontent.com/Vikash922/Attendance/main/update.json"

    suspend fun checkForUpdate(): UpdateInfo? = withContext(Dispatchers.IO) {
        try {
            val url = URL(UPDATE_JSON_URL)
            val connection = url.openConnection() as HttpURLConnection
            connection.requestMethod = "GET"
            connection.connectTimeout = 5000
            connection.readTimeout = 5000

            if (connection.responseCode == HttpURLConnection.HTTP_OK) {
                val reader = BufferedReader(InputStreamReader(connection.inputStream))
                val response = reader.readText()
                reader.close()

                val json = JSONObject(response)
                val latestVersionCode = json.getInt("versionCode")
                val latestVersionName = json.getString("versionName")
                val apkUrl = json.getString("apkUrl")
                val releaseNotes = json.optString("releaseNotes", "Minor bug fixes and UI improvements.")

                val currentVersionCode = BuildConfig.VERSION_CODE
                val hasUpdate = latestVersionCode > currentVersionCode

                return@withContext UpdateInfo(
                    hasUpdate = hasUpdate,
                    latestVersionCode = latestVersionCode,
                    latestVersionName = latestVersionName,
                    apkUrl = apkUrl,
                    releaseNotes = releaseNotes
                )
            }
        } catch (e: Exception) {
            Log.e("AppUpdater", "Error checking for update", e)
        }
        return@withContext null
    }

    fun downloadAndInstallUpdate(context: Context, apkUrl: String, version: String) {
        Toast.makeText(context, "Downloading update...", Toast.LENGTH_SHORT).show()
        val destination = File(context.getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS), "update_v$version.apk")
        if (destination.exists()) destination.delete()

        val request = DownloadManager.Request(Uri.parse(apkUrl))
            .setTitle("Laborbook Update")
            .setDescription("Downloading version $version")
            .setDestinationUri(Uri.fromFile(destination))
            .setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED)
            .setAllowedOverMetered(true)
            .setAllowedOverRoaming(true)

        val downloadManager = context.getSystemService(Context.DOWNLOAD_SERVICE) as DownloadManager
        val downloadId = downloadManager.enqueue(request)

        val onComplete = object : BroadcastReceiver() {
            override fun onReceive(c: Context, intent: Intent) {
                val id = intent.getLongExtra(DownloadManager.EXTRA_DOWNLOAD_ID, -1)
                if (downloadId == id) {
                    installApkFromDownloadManager(context, id)
                    context.unregisterReceiver(this)
                }
            }
        }

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            context.registerReceiver(onComplete, IntentFilter(DownloadManager.ACTION_DOWNLOAD_COMPLETE), Context.RECEIVER_EXPORTED)
        } else {
            context.registerReceiver(onComplete, IntentFilter(DownloadManager.ACTION_DOWNLOAD_COMPLETE))
        }
    }

    private fun installApkFromDownloadManager(context: Context, downloadId: Long) {
        try {
            val downloadManager = context.getSystemService(Context.DOWNLOAD_SERVICE) as DownloadManager
            val uri = downloadManager.getUriForDownloadedFile(downloadId)
            if (uri != null) {
                val intent = Intent(Intent.ACTION_VIEW).apply {
                    setDataAndType(uri, "application/vnd.android.package-archive")
                    flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_GRANT_READ_URI_PERMISSION
                }
                context.startActivity(intent)
            } else {
                Toast.makeText(context, "Failed to get download URI.", Toast.LENGTH_SHORT).show()
            }
        } catch (e: Exception) {
            Log.e("AppUpdater", "Error installing APK from DM", e)
            Toast.makeText(context, "Failed to launch installer automatically. Please install manually.", Toast.LENGTH_LONG).show()
        }
    }
}
