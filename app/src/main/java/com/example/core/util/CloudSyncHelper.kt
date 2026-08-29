package com.example.core.util

import android.content.Context
import androidx.work.Constraints
import androidx.work.ExistingPeriodicWorkPolicy
import androidx.work.NetworkType
import androidx.work.PeriodicWorkRequestBuilder
import androidx.work.WorkManager
import com.example.data.remote.CloudSyncWorker
import java.util.concurrent.TimeUnit

object CloudSyncHelper {
    private const val SYNC_WORK_NAME = "GuaranteedCloudSyncWork"

    fun schedulePeriodicSync(context: Context) {
        // Requires network connection to run
        val constraints = Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .build()

        // Runs every 12 hours
        val syncRequest = PeriodicWorkRequestBuilder<CloudSyncWorker>(12, TimeUnit.HOURS)
            .setConstraints(constraints)
            .build()

        WorkManager.getInstance(context).enqueueUniquePeriodicWork(
            SYNC_WORK_NAME,
            ExistingPeriodicWorkPolicy.KEEP, // Keep existing schedule if app restarts
            syncRequest
        )
    }
}
