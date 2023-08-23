from PIL import Image
from glob import glob
from sklearn.cluster import DBSCAN, KMeans
from typing import List

import imagehash
import cv2
import numpy

class Main:
    IMAGES_PATH = "tmp"


    def execute(self) -> None:
        target_dirs = glob(f"{self.IMAGES_PATH}/**/")
        images_per_dir = []
        image_vectors = []

        for target_dir in target_dirs:
            images = []
            for file in glob(f"{target_dir}/*.jpeg"):
                # 画像をロード
                image = Image.open(file)
                # 画像のハッシュを計算
                image_hash = imagehash.average_hash(image)
                images.append(image_hash)

                # 画像をリサイズ???
                image_vector = cv2.resize(cv2.imread(file), (64, 64), cv2.INTER_CUBIC)
                # ???
                image_vectors.append(image_vector.reshape(-1))

            images_per_dir.append(images)

        print(len(image_vectors))

        self.dbscan(image_vectors)
        self.kmeans(image_vectors)



    def dbscan(self, image_vectors) -> None:
        # クラスター化
        clustering = DBSCAN(eps=3, min_samples=2).fit(numpy.array(image_vectors))
        print(f"{clustering.labels_=}")
        print(f"{clustering=}")


    def kmeans(self, image_vectors) -> None:
        clustering = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(image_vectors)
        print(f"{clustering.labels_=}")
        labels = clustering.labels_
        # for idx, flip in enumerate(flips):
        #     print(labels[start: start + len(flip)])
        #     start += len(flip)


if __name__ == "__main__":
    Main().execute()
