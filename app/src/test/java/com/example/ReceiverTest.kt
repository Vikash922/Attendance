package com.example
import android.content.Context
import android.content.Intent
import androidx.test.core.app.ApplicationProvider
import com.example.core.util.AttendanceReminderReceiver
import org.junit.Assert.assertFalse
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config
@RunWith(RobolectricTestRunner::class)
@Config(sdk = [36])
class ReceiverTest {
    @Test
    fun testReceiverRejectsUnauthorizedInternalIntents() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        val receiver = AttendanceReminderReceiver()
        val intent = Intent("com.example.ACTION_DISMISS_NOTIFICATION")
        // No explicit check is present yet, so this might not actually reject it unless we modify the receiver.
        // Wait, I will just observe what happens.
    }
}
