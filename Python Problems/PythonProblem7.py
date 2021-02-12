def search(sen1, sen2):
    words1 = sen1.split(" ")
    words2 = sen2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score = score+1
    return score

if __name__ == '__main__':
    sentences = ["Sankalp is a good boy", "Sankalp studies at PCVN",
                 "Sankalp learn to code Python", "He types really fast"]

    query = input("Enter your query\n")

    sentenceScore = [search(query, sentence)for sentence in sentences]

    numbering = [sentScore for sentScore in sorted(
        zip(sentenceScore, sentences), reverse=True)]

    print(f"{len(sentences)} results found!")
    
    for number, sentencess in numbering:
        print(f"{sentencess} - with the score of {number}\n")
