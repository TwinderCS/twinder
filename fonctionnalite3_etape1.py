

def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag 
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        f = open("",'r') #nom du fichier mots clés
        content = f.readlines()
        result_file = open("",'a') #nom du fichier à mettre qui sert de résultat
        for ligne in content:
            result = API.tweet_collect_whole(ligne) #remplacer API
            result_file.write("\nresult")
        f.close()
        result_file.close()

        hashtags = open("",'r') #nom du fichier hashtags
        content = hashtags.readlines()
        result_hashtags = open("",'a') #nom du fichier à mettre qui sert de résultat
        for ligne in content:
            result_hash = API.tweet_collect_whole(ligne) #remplacer API
            result_hashtags.write("\nresult")
        hashtags.close()
        result_hashtags.close()

    except IOError:
        print("Error")
        pass
