# -*- coding: utf-8 -*-
"""Fitness_chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oCBF_iUTJryYasxs43AiedB6cnc0YEhs
"""

import random
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class FitnessChatbot:
    def __init__(self):
        self.greetings = ["Hi there!", "Hello!", "Hey!"]
        self.goodbyes = ["Goodbye!", "See you later!", "Take care!"]
        self.workout_responses = {
            "upper body": "You can try push-ups, pull-ups, and dumbbell curls.",
            "lower body": "Consider squats, lunges, and calf raises for your lower body.",
            "core": "For your core, try planks, crunches, and Russian twists.",
            "cardio": "For cardio, you can do activities like running, cycling, or jumping rope."
        }
        self.diet_responses = {
            "protein": "Include foods like chicken, fish, eggs, and tofu for protein.",
            "carbs": "Opt for complex carbs like whole grains, fruits, and vegetables.",
            "fats": "Healthy fat sources include avocados, nuts, seeds, and olive oil.",
            "hydration": "Remember to drink plenty of water throughout the day."
        }
        self.classifier = self.train_classifier()

    def train_classifier(self):
        # Training data for classifying user inputs
        X_train = [
            "workout routines", "dietary advice", "hello", "hi", "bye"
        ]
        y_train = ["workout", "diet", "greeting", "greeting", "goodbye"]

        # Vectorize the text data
        vectorizer = CountVectorizer()
        X_train_vectorized = vectorizer.fit_transform(X_train)

        # Train a simple classifier
        classifier = MultinomialNB()
        classifier.fit(X_train_vectorized, y_train)

        return classifier

    def classify_input(self, user_input):
        vectorizer = CountVectorizer()
        vectorized_input = vectorizer.transform([user_input])
        category = self.classifier.predict(vectorized_input)[0]
        return category

    def respond(self, user_input):
        category = self.classify_input(user_input)
        if category == "workout":
            return random.choice(list(self.workout_responses.values()))
        elif category == "diet":
            return random.choice(list(self.diet_responses.values()))
        elif category == "greeting":
            return random.choice(self.greetings)
        elif category == "goodbye":
            return random.choice(self.goodbyes)
        else:
            return "I'm sorry, I didn't understand that. Can you please ask again?"

    def run_chatbot(self):
        print("Welcome to Fitness Chatbot!")
        print("You can ask me about workout routines, dietary advice, or say goodbye to exit.")

        while True:
            user_input = input("You: ").lower()
            response = self.respond(user_input)
            print("Fitness Chatbot:", response)
            if "bye" in user_input:
                break

if __name__ == "__main__":
    chatbot = FitnessChatbot()
    chatbot.run_chatbot()
