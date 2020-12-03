from github import Github

g = Github('','')

repo = g.get_repo('saulo9220/Covid-peru')
contents = repo.get_contents("src/confirmados.csv")
