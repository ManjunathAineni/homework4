# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "The same individual can fulfill multiple rules simultaneously. For instance, if an individual is both a homeowner (Yes) and has a single marital status, both rules - Home Owner = Yes and Marital Status = Single - would yield DB = Yes."
    answers["(b) explain"] = "This system fails to encompass all potential combinations of attribute values, leaving certain scenarios unaccounted for. For instance, it does not cover the case of Marital Status = Divorced."
    answers["(c) explain"] = "When a person is neither a homeowner nor single, both Home Owner = No, Marital Status = Single and Marital Status = Single rules would result in DB = Yes. Thus, there might be a need for ordering in this set of rules."
    answers["(d) explain"] = " In situations where an individual is neither a homeowner nor single, there are no rules to determine the DB value. Consequently, a default class becomes necessary to handle such instances."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "To ensure mutual exclusivity among the rules, there should be no overlap between the conditions. They appear mutually exclusive as they categorize separate groups such as birds, fishes, mammals, and reptiles, each based on unique combinations of attributes"
    answers["(b) example"] = "There is no rule that covers amphibians, so under the given rules, a salamander would not be classified. This indicates that the rules are not exhaustive, as they do not provide a classification for every vertebrate in the dataset."
    answers["(c) example"] = "Because each rule assigns a different group without any overlap, the sequence in which they're used won't alter the classification result. Consequently, there's no need to worry about the order of these rules."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = " The back-propagation algorithm efficiently computes gradients by using the chain rule of calculus. It recursively applies the gradient of the loss from the output layer backward through the network, utilizing the gradient from each subsequent layer to compute the gradient of the preceding layer."
    answers["(b) explain"] = "Each layer's output is determined from the activations of the previous layer through weighted sums and activation functions. This creates a direct computational chain from the input layer to the output layer."
    answers["(c) explain"] = "The vanishing gradient problem arises when gradients of the loss function diminish significantly as they propagate through the layers of a deep neural network during training. This leads to slow or halted learning, particularly in the initial layers of the network. It's important to note that while training errors diminish to zero, substantial test errors remain, which is characteristic of overfitting rather than the vanishing gradient problem."
    answers["(d) explain"] = "The statement is largely inaccurate because achieving perfect classification doesn't necessarily result in zero gradients for all weights in a neural network. Gradients are influenced by various factors such as loss and activation functions, and even minor deviations or numerical precision issues can lead to non-zero gradients. These non-zero gradients allow for ongoing learning and fine-tuning of the network."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25
    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "Selecting k=5 strikes a balanced approach. It effectively reduces noise and outliers while preserving local detail, unlike the extreme case of k=1. Additionally, k=5 prevents oversmoothing, a risk associated with larger k values such as k=50."
    answers["(b) explain"] = "Considering the overlap between the two data categories, employing a large k value like 50 is unnecessary. Such a choice may lead to errors and an over-smoothing effect, potentially obscuring the distinction between classes, particularly in densely packed class regions."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = " There are 3 instance of A when positive and total of 5 positive instance"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0 
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "Naive Bayes of positive instance is 0.192 whereas for negative it is 0.032"
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] = "P(X|YZ) is not equal to P(X|Z), So no "
  
    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    #answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    #answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict,f)
