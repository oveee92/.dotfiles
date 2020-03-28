config.bind('gi', 'set downloads.location.directory ~/Pictures ;; hint images download')
config.bind('gd', 'set downloads.location.directory ~/Downloads ;; hint images download')

c.url.default_page = 'https://www.google.com/'
c.url.searchengines = {
        'DEFAULT': 'https://google.com/search?&q={}',
        'i': 'https://google.com/search?q={}&tbm=isch',
        'images': 'https://google.com/search?q={}&tbm=isch',
        'maps': 'https://www.google.com/maps/search/{}',
        'aw': 'https://wiki.archlinux.org/index.php?search={}',
        'y': 'https://www.youtube.com/results?search_query={}',
        'yr': 'https://www.yr.no/soek/soek.aspx?sted={}',
        'ÿ́outube': 'https://www.youtube.com/results?search_query={}',
        'spotify': 'https://open.spotify.com/search/results/{}'
        }

c.aliases = {
        'w': 'session-save',
        'q': 'quit',
        'wq': 'quite --save'
        }

c.fonts.tabs = '12pt monospace'
