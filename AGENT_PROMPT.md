# Hey PC Assistant - AI Agent Prompt

## System Description
Hey PC Assistant is a voice-activated Windows PC automation assistant that responds to wake words and executes system commands through natural language processing.

## Core Capabilities

### Voice Interaction
- **Wake Word Detection**: Listens for "Hey PC" to activate
- **Voice Recognition**: Uses Google Speech Recognition API to convert speech to text
- **Text-to-Speech**: Provides audio feedback using pyttsx3 engine

### Supported Commands

1. **File Operations**
   - `"open file"` or `"open"` - Opens any file or directory on the system
   - Validates file paths and provides clear error messages
   - Handles edge cases like incomplete paths (e.g., 'c') gracefully
   
2. **File Manager**
   - `"open file manager"` or `"file manager"` - Launches Windows Explorer at C:\
   - Quick access to system file browser
   
3. **Weather Information**
   - `"weather"` - Checks weather information (placeholder for API integration)

### Key Features

- **Robust Error Handling**: 
  - Validates user input before execution
  - Provides specific feedback for different failure modes
  - Normalizes file paths using `os.path.normpath()`
  - Checks file/directory existence before attempting to open

- **Flexible Command Parsing**:
  - Case-insensitive command matching
  - Supports multiple phrasings for the same action
  - Handles empty or null inputs gracefully

- **User Feedback**:
  - Clear voice and text responses for all operations
  - Specific error messages (invalid path, file not found, unsupported command)
  - Continuous listening loop for ongoing interaction

## Example Interactions

```
User: "Hey PC"
Assistant: "Yes, how can I help you?"

User: "Open file manager"
Assistant: "Opening File Manager"
[Windows Explorer opens at C:\]

User: "Open file"
Assistant: "Which file would you like to open?"
User: "C:\Users\Documents\report.pdf"
Assistant: "File opened successfully"

User: "Open"
Assistant: "Which file would you like to open?"
User: "c"
Assistant: "Sorry, I couldn't open that file. Please check the path and try again."
[Console: Invalid file path: 'c' is too short or incomplete.]
```

## Technical Architecture

### Components
1. **assistant.py** - Main entry point and control loop
2. **wake_word.py** - Wake word detection logic
3. **voice_recognition.py** - Speech-to-text using SpeechRecognition library
4. **nlp_processing.py** - Command routing and parsing
5. **task_automation.py** - Task execution functions
6. **text_to_speech.py** - Audio response generation

### Dependencies
- `speechrecognition` - Voice input processing
- `pyttsx3` - Text-to-speech output
- `os` - System file operations (Windows-specific `startfile()`)

## Use Cases

- Hands-free file navigation while working
- Quick access to frequently used files and directories
- System automation for common tasks
- Accessibility tool for users who prefer voice commands

## Future Enhancements
- Web search integration
- Application launching (browsers, programs)
- System controls (volume, brightness)
- Calendar and reminder management
- Email and messaging capabilities
- Custom command macros

---

**Status**: Production-ready with robust error handling and comprehensive command support for Windows environments.
