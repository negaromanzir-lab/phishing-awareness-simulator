# Phishing Awareness Simulator

A beginner-friendly Python cybersecurity project that teaches users to recognize phishing and social-engineering warning signs through fictional email scenarios.

## Features

- Five simulated email scenarios.
- Interactive phishing-awareness quiz.
- Basic detection of urgency, sensitive-information requests, suspicious links, prize claims, and risky attachment instructions.
- Educational explanations after each answer.
- Randomized scenario order.
- Final score and learning feedback.

## Requirements

- Python 3.10 or later recommended.
- No third-party packages required.

## Run the Application

```bash
python phishing_simulator.py
```

Enter `P` for phishing/suspicious or `L` for legitimate-looking.

## Learning Objectives

- Understand common phishing techniques.
- Recognize social-engineering warning signs.
- Practice Python functions, regular expressions, loops, and conditionals.
- Build an interactive command-line application.
- Understand the limitations of rule-based detection.

## Safety

This project uses fictional messages and reserved example domains. It does not send emails, collect credentials, or open links.

The keyword-based detection is educational and can produce false positives and false negatives. A message that appears legitimate is not necessarily safe.

## Future Improvements

- Add automated unit tests.
- Load scenarios from a JSON file.
- Track results across training sessions without storing sensitive information.
- Add a graphical interface.
- Improve detection rules and explain their limitations.

## License

MIT License, if distributed with an MIT `LICENSE` file.