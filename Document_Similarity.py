import sys

def read_file(filename):
    """This function is used to read the text file"""
    try:
        with open(filename, "r", errors='ignore') as file:
            data = file.read()
        return data

    except IOError:
        print("Error opening or reading input file: ", filename)
        sys.exit()


#sample_1 = read_file('Sample1.txt')
#sample_2 = read_file('Sample2.txt')
#sample_3 = read_file('Sample3.txt')
stopwords = read_file('stopwords.txt')


# step a: function to remove punctuation/apostrophe/convert to lower

def removal(data):
    """This function converts uppercase to lowercase, replaces apostrophe and removes punctuation"""
    y = data

    ##step 1: converting to lower case
    y = y.lower()

    # step 2: initializing punctuations string  
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

    # step 3: remove_punctuation  
    for val in y:
        if val in punc:
            y = y.replace(val, " ")

    return y


#sample_1 = removal(sample_1)
#sample_2 = removal(sample_2)
#sample_3 = removal(sample_3)


def process(text):
    """ This fucntion is for tokenization, removing stop words"""

    x = text.split()

    # step5: filtering out tokens that are not alphabetic
    x = [c for c in x if c.isalpha()]

    # step6: removing stop words
    list_stop_words = stopwords.splitlines()
    x = [w for w in x if not w in list_stop_words]

    return x


#sample_1 = process(sample_1)
#sample_2 = process(sample_2)
#sample_3 = process(sample_3)


# Method - Using Vector distance

def freq_count(text):
    """This function is to form key value pairs in terms of words in document and their respective frequency"""
    Dict = {}

    for word in text:
        if word in Dict:
            Dict[word] = Dict[word] + 1
        else:
            Dict[word] = 1

    return Dict


def dotproduct(d1, d2):
    """This function calculates dot product based on frequency of words in two documents. If the key is same in both documnets 
    then function will simply multiply the frequency values """
    d1 = freq_count(d1)
    d2 = freq_count(d2)
    total = 0.0
    for key in d1:
        if key in d2:
            total += (d1[key] * d2[key])
    return total


def percent_similar(D1, D2):
    """This function calculates  with the help of dot product. Same documents will show 100% similarity"""
    numerator = dotproduct(D1, D2)
    denominator = (dotproduct(D1, D1) * dotproduct(D2, D2)) ** (1 / 2)
    return (numerator / denominator)


# between sample_1 and sample_2
#a = percent_similar(sample_1, sample_2)
#output = round(a * 100, 2)
#print("The documents show  " + str(output) + " percent similarity.")

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

#using POST method
@app.route('/predict', methods =['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == "POST":
        message1 = request.form["message 1"]
        message2 = request.form["message 2"]
        sample_1 = message1
        sample_2 = message2

        sample_1 = removal(sample_1)
        sample_2 = removal(sample_2)

        sample_1 = process(sample_1)
        sample_2 = process(sample_2)

        prediction = percent_similar(sample_1, sample_2)

    return render_template('index.html', prediction_text=prediction)

if __name__ == "__main__":
    app.run(debug=True)