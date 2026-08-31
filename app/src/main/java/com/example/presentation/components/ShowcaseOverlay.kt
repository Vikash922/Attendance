package com.example.presentation.components

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Rect
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.BlendMode
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.layout.boundsInRoot
import androidx.compose.ui.layout.onGloballyPositioned
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

class ShowcaseState {
    var targets by mutableStateOf<Map<String, Rect>>(emptyMap())
    var currentStepIndex by mutableStateOf(0)
    var isVisible by mutableStateOf(false)
    var steps by mutableStateOf<List<ShowcaseStep>>(emptyList())
    
    fun registerTarget(id: String, bounds: Rect) {
        targets = targets.toMutableMap().apply { put(id, bounds) }
    }
    
    fun startTour(tourSteps: List<ShowcaseStep>) {
        if (tourSteps.isEmpty()) return
        steps = tourSteps
        currentStepIndex = 0
        isVisible = true
    }
    
    fun nextStep() {
        if (currentStepIndex < steps.size - 1) {
            currentStepIndex++
        } else {
            isVisible = false
        }
    }
    
    fun skipTour() {
        isVisible = false
    }
}

data class ShowcaseStep(
    val targetId: String,
    val title: String,
    val description: String
)

val LocalShowcaseState = compositionLocalOf { ShowcaseState() }

@Composable
fun Modifier.showcaseTarget(id: String): Modifier {
    val showcaseState = LocalShowcaseState.current
    return this.onGloballyPositioned { coordinates ->
        showcaseState.registerTarget(id, coordinates.boundsInRoot())
    }
}

@Composable
fun ShowcaseOverlay() {
    val state = LocalShowcaseState.current
    if (!state.isVisible || state.steps.isEmpty()) return

    val currentStep = state.steps.getOrNull(state.currentStepIndex) ?: return
    val targetBounds = state.targets[currentStep.targetId]

    Box(
        modifier = Modifier
            .fillMaxSize()
            .graphicsLayer(alpha = 0.99f) // Required for BlendMode.Clear to work in Canvas
    ) {
        Canvas(modifier = Modifier.fillMaxSize()) {
            drawRect(color = Color.Black.copy(alpha = 0.75f), size = size)
            
            if (targetBounds != null) {
                // Add some padding around the target
                val padding = 8.dp.toPx()
                drawRoundRect(
                    color = Color.Transparent,
                    topLeft = Offset(targetBounds.left - padding, targetBounds.top - padding),
                    size = Size(targetBounds.width + padding * 2, targetBounds.height + padding * 2),
                    cornerRadius = CornerRadius(12.dp.toPx(), 12.dp.toPx()),
                    blendMode = BlendMode.Clear
                )
            }
        }
        
        // Tooltip Content
        if (targetBounds != null) {
            val density = LocalDensity.current
            val screenHeight = with(density) { LocalContext.current.resources.displayMetrics.heightPixels.toDp() }
            val topSpace = with(density) { targetBounds.top.toDp() }
            val bottomSpace = screenHeight - with(density) { targetBounds.bottom.toDp() }
            
            val isTooltipBelow = bottomSpace > topSpace
            
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(24.dp),
                contentAlignment = if (isTooltipBelow) Alignment.TopCenter else Alignment.BottomCenter
            ) {
                Column(
                    modifier = Modifier
                        .padding(
                            top = if (isTooltipBelow) with(density) { (targetBounds.bottom + 16f).toDp() } else 0.dp,
                            bottom = if (!isTooltipBelow) with(density) { (LocalContext.current.resources.displayMetrics.heightPixels - targetBounds.top + 16f).toDp() } else 0.dp
                        )
                        .background(Color.White, RoundedCornerShape(16.dp))
                        .padding(20.dp)
                ) {
                    Text(
                        text = currentStep.title,
                        fontSize = 18.sp,
                        fontWeight = FontWeight.Bold,
                        color = Color(0xFF1D61E7)
                    )
                    Spacer(modifier = Modifier.height(8.dp))
                    Text(
                        text = currentStep.description,
                        fontSize = 14.sp,
                        color = Color(0xFF333333),
                        lineHeight = 20.sp
                    )
                    Spacer(modifier = Modifier.height(20.dp))
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            text = "Skip Tour",
                            fontSize = 14.sp,
                            color = Color.Gray,
                            modifier = Modifier.clickable { state.skipTour() }.padding(8.dp)
                        )
                        Button(
                            onClick = { state.nextStep() },
                            colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF1D61E7)),
                            shape = RoundedCornerShape(24.dp)
                        ) {
                            Text(
                                text = if (state.currentStepIndex == state.steps.size - 1) "Got it!" else "Next",
                                fontWeight = FontWeight.Bold,
                                color = Color.White
                            )
                        }
                    }
                }
            }
        } else {
             // Fallback if target not found (e.g. scrolled out of view)
             // We can just center the text
             Box(modifier = Modifier.fillMaxSize().padding(24.dp), contentAlignment = Alignment.Center) {
                 Column(
                    modifier = Modifier
                        .background(Color.White, RoundedCornerShape(16.dp))
                        .padding(20.dp)
                ) {
                    Text(text = currentStep.title, fontSize = 18.sp, fontWeight = FontWeight.Bold, color = Color(0xFF1D61E7))
                    Spacer(modifier = Modifier.height(8.dp))
                    Text(text = currentStep.description, fontSize = 14.sp, color = Color(0xFF333333))
                    Spacer(modifier = Modifier.height(20.dp))
                    Button(onClick = { state.nextStep() }, modifier = Modifier.align(Alignment.End)) {
                        Text(if (state.currentStepIndex == state.steps.size - 1) "Got it!" else "Next")
                    }
                }
             }
        }
    }
}
