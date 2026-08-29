package com.example.data.remote

import android.content.Context
import android.util.Log
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import com.example.data.repository.LaborRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

class CloudSyncWorker(
    appContext: Context,
    workerParams: WorkerParameters
) : CoroutineWorker(appContext, workerParams) {

    override suspend fun doWork(): Result = withContext(Dispatchers.IO) {
        try {
            Log.d("CloudSyncWorker", "Starting guaranteed background sync...")
            val repository = LaborRepository(applicationContext)
            
            // This will trigger the sync logic built into the repository
            // including updating the root metadata in Firebase.
            repository.triggerCloudSyncBackground()
            
            Log.d("CloudSyncWorker", "Guaranteed background sync completed successfully.")
            Result.success()
        } catch (e: Exception) {
            Log.e("CloudSyncWorker", "Background sync failed: ${e.message}")
            // If it's a transient network issue, retry later
            Result.retry()
        }
    }
}
