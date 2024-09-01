import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def load_faqs_from_file(filename):
    with open(filename, 'r') as file:
        faqs = []
        lines = file.readlines()
        
        question = None
        answer = ""
        
        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace
            
            if line.startswith("Q:"):
                if question:
                    faqs.append({"question": question, "answer": answer.strip()})
                question = line[2:].strip()  # Extract the question text
                answer = ""  # Reset the answer for the new question
                
            elif line.startswith("A:"):
                answer = line[2:].strip()  # Start the answer text
                
            else:
                if answer:
                    answer += " " + line  # Continue the answer on new lines
        
        # Append the last question-answer pair
        if question:
            faqs.append({"question": question, "answer": answer.strip()})
    
    return faqs



filename = 'Amazon_sagemaker_Faq.txt'
faqs = load_faqs_from_file(filename)


# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

# Preprocess text
def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return ' '.join(tokens)
# Preprocess all FAQ questions
preprocessed_faqs = [preprocess_text(faq['question']) for faq in faqs]

# Vectorize the FAQs using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_faqs)

def get_response(user_query, faqs):
    preprocessed_faqs = [preprocess_text(faq['question']) for faq in faqs]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_faqs)
    
    preprocessed_query = preprocess_text(user_query)
    query_vector = vectorizer.transform([preprocessed_query])
    
    similarities = cosine_similarity(query_vector, tfidf_matrix)
    best_match_idx = similarities.argmax()
    
    return faqs[best_match_idx]['answer']
def chat():
    print("Welcome to the FAQ chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()
