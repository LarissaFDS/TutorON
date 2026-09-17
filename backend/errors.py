"""Expected dependency failures; programming errors are deliberately not wrapped."""


class AIServiceError(Exception):
    status_code = 502
    code = "AI_SERVICE_ERROR"
    public_message = "The AI service failed to process the request."


class ConfigurationError(AIServiceError):
    status_code = 500
    code = "CONFIGURATION_ERROR"
    public_message = "Backend configuration is invalid. Check the server configuration."


class GeminiUnavailableError(AIServiceError):
    status_code = 503
    code = "AI_TEMPORARILY_UNAVAILABLE"
    public_message = "Gemini is temporarily unavailable. Please try again shortly."


class GeminiRequestError(AIServiceError):
    code = "GEMINI_REQUEST_ERROR"
    public_message = "Gemini rejected the request. Check API credentials and model configuration."


class RAGError(AIServiceError):
    code = "RAG_ERROR"
    public_message = "Course material retrieval failed. Check Supabase and the indexed material."
