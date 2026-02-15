# Mail Merge

A utility that generates personalized letters by merging recipient names into a template letter.

## Features
- Bulk letter generation from names list
- Template placeholder replacement
- Automated file naming for each letter
- Support for batch processing

## Project Structure
- `main.py` - Main merge logic
- `Input/Names/invited_names.txt` - List of recipient names (one per line)
- `Input/Letters/starting_letter.txt` - Letter template with [name] placeholder
- `Output/ReadyToSend/` - Generated letters output directory

## Requirements
- Python 3.x

## Installation & Setup
1. Clone or download the project
2. Create required directories:
   ```bash
   mkdir -p Input/Names Input/Letters Output/ReadyToSend
   ```
3. Create `Input/Names/invited_names.txt` with names (one per line)
4. Create `Input/Letters/starting_letter.txt` with template using [name] placeholder

## Usage
```bash
python main.py
```

## File Formats

### invited_names.txt
```
Alice
Bob
Charlie
```

### starting_letter.txt
```
Dear [name],

We are pleased to invite you to our special event...

Best regards,
The Organizing Committee
```

## Output
Generated files will appear in `Output/ReadyToSend/` with names like:
- letter_for_Alice.docx
- letter_for_Bob.docx
- letter_for_Charlie.docx

## Notes
- Names are stripped of whitespace/newlines
- Case is preserved from the names list
- Original template file is not modified

