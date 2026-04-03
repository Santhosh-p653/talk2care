package com.example.talk2care;
import java.util.List;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
public class ChatController {

	@PostMapping("/process")
	public String process(@RequestBody Map<String, String> body) {

	    String msg = body.get("message").toLowerCase();

	    // Critical mental health detection
	    if (msg.contains("suicide") || msg.contains("kill myself") || msg.contains("die")) {
	        return "I'm really sorry you're feeling this way. Please consider reaching out to a trusted person or a mental health professional immediately. You are not alone ❤️";
	    }

	    // Mental stress indicators
	    if (msg.contains("stress") || msg.contains("anxiety") || msg.contains("tired")) {
	        return "It sounds like you're going through stress. Try taking a short break, breathing exercises, or talking to someone you trust.";
	    }

	    // General sadness
	    if (msg.contains("sad") || msg.contains("lonely")) {
	        return "I'm here for you. Talking about it can really help. Would you like to share more?";
	    }

	    // Positive state
	    if (msg.contains("happy") || msg.contains("good")) {
	        return "That's great to hear! Keeping a positive mindset is important for your health 😊";
	    }

	    return "Tell me more about how you're feeling.";
	}
	
	@PostMapping("/summary")
	public String generateSummary(@RequestBody List<Map<String, String>> chat) {

	    StringBuilder summary = new StringBuilder();

	    summary.append("=== Talk2Care Health Report ===\n\n");

	    int sadCount = 0;
	    int stressCount = 0;

	    for (Map<String, String> msg : chat) {

	        if (msg.get("type").equals("user")) {

	            String text = msg.get("text").toLowerCase();

	            summary.append("User: ").append(text).append("\n");

	            if (text.contains("sad") || text.contains("lonely")) sadCount++;
	            if (text.contains("stress") || text.contains("tired")) stressCount++;
	        }
	    }

	    summary.append("\n--- Analysis ---\n");

	    if (sadCount > 0) {
	        summary.append("Signs of sadness detected.\n");
	    }

	    if (stressCount > 0) {
	        summary.append("Signs of stress detected.\n");
	    }

	    if (sadCount == 0 && stressCount == 0) {
	        summary.append("No major emotional distress detected.\n");
	    }

	    summary.append("\nRecommendation: Maintain healthy habits and consult a professional if needed.\n");

	    return summary.toString();
	}
}