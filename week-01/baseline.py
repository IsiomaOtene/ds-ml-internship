scores = [64, 72, 55, 91, 72, 83, 47, 76]
def summarize_scores(scores):
    count = len(scores)
    minimum = min(scores)
    maximum = max(scores)
    mean = sum(scores) / len(scores)
    return minimum, maximum, mean
def classify_scores(score):
    if score >= 80:
        return "excellent"
    elif score >= 65 and score <= 79:
        return "good"
    else:
        return "needs improvement"
    for score in scores:
        classification = classify_scores(score)
        print("Scores: ", score, "is", classification)
scores_counts = {"excellent"  : 0, "good" : 0, "needs improvement" : 0}
for score in scores:
    classification = classify_scores(score)
    scores_counts[classification] += 1
unique_scores = set(scores)
print("Unique numbers: ", unique_scores)
print("Score counts: ", scores_counts)

    