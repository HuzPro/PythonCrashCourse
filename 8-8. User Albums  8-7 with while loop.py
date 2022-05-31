def makeAlbum(artistName, albumName, TrackNo=''):
    if artistName and albumName:
        album = {'albumName': albumName, "artistName": artistName}
    if TrackNo:
        album['trackno'] = TrackNo
    return album



while True:
    print("\n(Enter 'q' at any time to exit the program)\n")
    albumName = input("Enter the name of the album: ")
    if albumName == 'q' or albumName == 'Q':
        break
    
    artistName = input("\nEnter the album's artist's name: ")
    if artistName == 'q' or artistName == 'Q':
        break
    numberOfTracks = input("\nEnter the number of tracks in the album(Optional): ")
    if numberOfTracks == 'q' or numberOfTracks == 'Q':
        break
    album = makeAlbum(albumName, artistName, numberOfTracks)
    print(album)

