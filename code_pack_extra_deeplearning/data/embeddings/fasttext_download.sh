# Script to download Fastext
URL=https://dl.fbaipublicfiles.com/fasttext/vectors-english
EMBEDDINGS=wiki-news-300d-1M.vec

# download and extract
if [ ! -f $EMBEDDINGS ]; then
  wget $URL/$EMBEDDINGS.zip
  unzip $EMBEDDINGS.zip
  rm $EMBEDDINGS.zip
fi
