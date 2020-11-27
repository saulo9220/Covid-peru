from git import Repo,remote

rw_dir = 'D:\Proyectos\GitHub\Covid-peru'
repo = Repo(rw_dir)



origin = repo.remote(name='origin')

origin.Commit.message('cambio')
origin.pull()
origin.push()
