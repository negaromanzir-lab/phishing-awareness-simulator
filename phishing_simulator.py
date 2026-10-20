
import re
import random


SCENARIOS = [
    {
        "subject": "Urgent: Account Suspension",
        "sender": "Security Team <security@example.invalid>",
        "message": (
            "Your account will be suspended today! "
            "Verify your password immediately at "
            "http://example.invalid/verify"
        ),
        "answer": "p",
        "explanation": (
            "The message creates urgency, requests a password, "
            "and includes an untrusted-looking link. Legitimate "
            "services should not ask you to disclose your password "
            "through an email link."
        ),
    },
    {
        "subject": "You Won a Prize!",
        "sender": "Prize Office <winner@example.invalid>",
        "message": (
            "Congratulations! You won a prize. "
            "Send your personal information immediately to claim it."
        ),
        "answer": "p",
        "explanation": (
            "Unexpected prizes and requests for personal information "
            "are warning signs. Verify promotions through an official "
            "website you navigate to independently."
        ),
    },
    {
        "subject": "Project Meeting Reminder",
        "sender": "Colleague <colleague@example.invalid>",
        "message": (
            "Reminder: our project meeting is tomorrow at 10 AM. "
            "Please review the agenda we discussed."
        ),
        "answer": "l",
        "explanation": (
            "This fictional message contains no obvious phishing "
            "indicators. However, a realistic message can still be "
            "malicious, so verify unexpected attachments or requests."
        ),
    },
    {
        "subject": "Unusual Sign-in Alert",
        "sender": "Account Alerts <alerts@example.invalid>",
        "message": (
            "We noticed a sign-in attempt. If this was not you, "
            "open your service's official app or website directly "
            "to review your account activity."
        ),
        "answer": "l",
        "explanation": (
            "This example recommends checking through the official "
            "app or website instead of following an embedded link. "
            "Still, sender names alone cannot prove authenticity."
        ),
    },
    {
        "subject": "Invoice: Enable Macros",
        "sender": "Billing <billing@example.invalid>",
        "message": (
            "Open the attached invoice and enable macros immediately "
            "to view your payment details."
        ),
        "answer": "p",
        "explanation": (
            "Unexpected attachments and instructions to enable macros "
            "are suspicious. Do not enable macros just to view a file; "
            "verify the request with the sender through a trusted channel."
        ),
    },
]


def detect_warning_signs(scenario):
    """Find basic warning signs in a simulated message."""
    text = (
        scenario["subject"] + " " +
        scenario["sender"] + " " +
        scenario["message"]
    ).lower()

    warnings = []

    if re.search(
        r"\b(urgent|immediately|today|suspended|closed)\b",
        text
    ):
        warnings.append(
            "Urgency or pressure to act quickly"
        )

    if re.search(
        r"\b(password|verify your account|personal information|"
        r"credit card|bank details)\b",
        text
    ):
        warnings.append(
            "Request for sensitive information"
        )

    if re.search(r"https?://", text):
        warnings.append(
            "Contains a link that should be checked carefully"
        )

    if re.search(
        r"\b(prize|won|winner|claim your prize)\b",
        text
    ):
        warnings.append(
            "Unexpected prize or reward claim"
        )

    if re.search(
        r"\b(attachment|enable macros|open the attached)\b",
        text
    ):
        warnings.append(
            "Potentially risky attachment or macro instruction"
        )

    return warnings


def run_simulation():
    print("=" * 52)
    print("        PHISHING AWARENESS SIMULATOR")
    print("=" * 52)
    print("Training mode: fictional messages only.")
    print("P = Phishing/suspicious, L = Legitimate-looking\n")

    questions = SCENARIOS.copy()
    random.shuffle(questions)

    score = 0

    for number, scenario in enumerate(questions, start=1):
        print("\n" + "-" * 52)
        print(f"Scenario {number} of {len(questions)}")
        print(f"From: {scenario['sender']}")
        print(f"Subject: {scenario['subject']}")
        print(f"\nMessage:\n{scenario['message']}")

        warnings = detect_warning_signs(scenario)

        answer = ""
        while answer not in ("p", "l"):
            answer = input(
                "\nIs this phishing/suspicious (P) "
                "or legitimate-looking (L)? "
            ).strip().lower()

            if answer not in ("p", "l"):
                print("Please enter P or L.")

        if answer == scenario["answer"]:
            print("\nCorrect!")
            score += 1
        else:
            print("\nNot quite. Review the explanation below.")

        print("\nLearning notes:")
        if warnings:
            for warning in warnings:
                print(f"- Warning sign: {warning}")
        else:
            print("- No obvious warning signs detected by basic rules.")

        print("\nExplanation:")
        print(scenario["explanation"])

        print(
            "\nRemember: these rules are educational clues, "
            "not proof that a message is safe or malicious."
        )

    print("\n" + "=" * 52)
    print("             TRAINING RESULTS")
    print("=" * 52)
    print(f"Your score: {score}/{len(questions)}")

    percentage = score / len(questions) * 100

    if percentage == 100:
        print("Excellent! You identified every example correctly.")
    elif percentage >= 60:
        print("Good work! Review the explanations for missed answers.")
    else:
        print("Keep practicing and review each warning sign.")

    print("\nSafety reminder:")
    print("Never share passwords or one-time codes through")
    print("unexpected messages. Verify requests independently.")


if __name__ == "__main__":
    run_simulation()
