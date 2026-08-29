sed -i '/suspend fun backupToCloud(): Result<com.example.data.remote.CloudBackupRecord> {/i \
    suspend fun syncMetadataToCloud() {\
        _isCloudSyncing.value = true\
        try {\
            com.example.data.remote.FirestoreSyncService.syncMetadataOnly(_userProfile.value, _workers.value, _transactions.value, context)\
        } catch(e: Exception) {\
            Log.w(TAG, "Metadata sync failed", e)\
        } finally {\
            _isCloudSyncing.value = false\
        }\
    }\
' app/src/main/java/com/example/data/repository/LaborRepository.kt
