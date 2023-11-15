from main import spotifyBot

if __name__ == '__main__':
    func = spotifyBot()
    func.startDriver()
    func.startBrowser()
    func.login()
    func.runBot()
    func.cursor_coor()
    func.closeDriver()