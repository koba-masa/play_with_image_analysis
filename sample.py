def sample():
    flips = []
    flips_for_dbscan = []

    for i in range(5):
        flip = []
        for filename in glob.glob("" + str(i+1) + "/*"):
            im = Image.open(filename)
            #im = im.reshape(-1)
            flip.append(imagehash.average_hash(im))
            image_vector = cv2.resize(cv2.imread(filename), (64, 64), cv2.INTER_CUBIC)
            flips_for_dbscan.append(image_vector.reshape(-1))
        flips.append(flip)

    print(len(flips_for_dbscan))
    clustering = DBSCAN(eps=3, min_samples=2).fit(np.array(flips_for_dbscan))
    print(f"{clustering.labels_=}")
    labels = clustering.labels_
    start = 0
    # for idx, flip in enumerate(flips):
    #     print(labels[start: start + len(flip)])
    #     start += len(flip)
    print(f"{clustering=}")


    kmeans = KMeans(n_clusters=15, random_state=0, n_init="auto").fit(flips_for_dbscan)
    print(f"{kmeans.labels_=}")
    labels = kmeans.labels_
    for idx, flip in enumerate(flips):
        print(labels[start: start + len(flip)])
        start += len(flip)
