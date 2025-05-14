#!/usr/bin/env python3
import random
import json
import os

class ItalianVocabLearner:
    def __init__(self, vocab_file='italian_vocab.json'):
        """
        Initialize the vocabulary learner.

        Args:
            vocab_file (str): Path to the JSON file storing vocabulary words.
        """
        self.vocab_file = vocab_file
        self.vocab = self.load_vocabulary()
        self.score = 0
        self.total_questions = 0

    def load_vocabulary(self):
        """
        Load vocabulary from a JSON file.
        If the file doesn't exist, create a default vocabulary.

        Returns:
            dict: A dictionary of Italian words and their English translations.
        """
        if os.path.exists(self.vocab_file):
            with open(self.vocab_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Default vocabulary to start with
            default_vocab = {
                "ciao": "hello",
                "grazie": "thank you",
                "per favore": "please",
                "acqua": "water",
                "pane": "bread",
                "casa": "house",
                "amico": "friend",
                "famiglia": "family",
                "buongiorno": "good morning",
                "buonasera": "good evening"
            }

            # Save the default vocabulary to a file
            with open(self.vocab_file, 'w', encoding='utf-8') as f:
                json.dump(default_vocab, f, ensure_ascii=False, indent=4)

            return default_vocab

    def add_word(self, italian_word, english_translation):
        """
        Add a new word to the vocabulary.

        Args:
            italian_word (str): The Italian word to add.
            english_translation (str): The English translation of the word.
        """
        # Convert to lowercase to avoid duplicates due to capitalization
        italian_word = italian_word.lower().strip()
        english_translation = english_translation.lower().strip()

        # Add the word to the vocabulary dictionary
        self.vocab[italian_word] = english_translation

        # Save the updated vocabulary to the file
        with open(self.vocab_file, 'w', encoding='utf-8') as f:
            json.dump(self.vocab, f, ensure_ascii=False, indent=4)

        print(f"Added: {italian_word} = {english_translation}")

    def remove_word(self, italian_word):
        """
        Remove a word from the vocabulary.

        Args:
            italian_word (str): The Italian word to remove.
        """
        italian_word = italian_word.lower().strip()

        if italian_word in self.vocab:
            del self.vocab[italian_word]

            # Save the updated vocabulary to the file
            with open(self.vocab_file, 'w', encoding='utf-8') as f:
                json.dump(self.vocab, f, ensure_ascii=False, indent=4)

            print(f"Removed: {italian_word}")
        else:
            print(f"Word '{italian_word}' not found in vocabulary.")

    def practice_translation(self):
        """
        Practice translating words from Italian to English.
        Provides random word selection and tracks score.
        """
        if not self.vocab:
            print("No words in vocabulary. Add some words first!")
            return

        # Select a random word from the vocabulary
        italian_word = random.choice(list(self.vocab.keys()))
        correct_translation = self.vocab[italian_word]

        print(f"\nTranslate the following Italian word to English:")
        print(f"Italian: {italian_word}")

        # Increment total questions
        self.total_questions += 1

        # Get user's translation attempt
        user_translation = input("Your translation: ").lower().strip()

        # Check if translation is correct
        if user_translation == correct_translation:
            print("✅ Correct!")
            self.score += 1
        else:
            print(f"❌ Incorrect. The correct translation is: {correct_translation}")

        # Display current score
        print(f"\nScore: {self.score}/{self.total_questions}")

    def view_vocabulary(self):
        """
        Display all words in the vocabulary.
        """
        if not self.vocab:
            print("No words in vocabulary.")
            return

        print("\n--- Vocabulary List ---")
        for italian, english in sorted(self.vocab.items()):
            print(f"{italian} = {english}")

    def menu(self):
        """
        Main menu for the vocabulary learning application.
        """
        while True:
            print("\n--- Italian Vocabulary Learner ---")
            print("1. Practice Vocabulary")
            print("2. Add New Word")
            print("3. Remove Word")
            print("4. View Vocabulary")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.practice_translation()
            elif choice == '2':
                italian = input("Enter Italian word: ").lower().strip()
                english = input("Enter English translation: ").lower().strip()
                self.add_word(italian, english)
            elif choice == '3':
                word = input("Enter Italian word to remove: ").lower().strip()
                self.remove_word(word)
            elif choice == '4':
                self.view_vocabulary()
            elif choice == '5':
                print("Grazie! Keep learning Italian!")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    learner = ItalianVocabLearner()
    learner.menu()

if __name__ == "__main__":
    main()
