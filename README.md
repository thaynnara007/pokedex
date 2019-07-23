# Pokedex

Pokedex it's a artificial intelligence that has as goal recognizing some pokemons images.

> This is a project that was developed for Inteligência Artificial course from UFCG

---

## Usage

- The model produced can recognize among seven pokemons, which are: pikachu, charmander, squirtle, bulbasaur, cyndaquil, totodile and chikorita.
- The searchimages package has some scripts that can be used for collecting images for the dataset.
- Since the trained model is to big for a commit , it will be find on google drive.
- [Trained model](https://drive.google.com/file/d/1DA2EeCIO4FF8kHjEIJm82oFO_K7hvA-r/view?usp=sharing)

> To classify images
```shell
$ python3 classifier.py --model path_to_pokedex.model --labelbin lb.pickle --image examples/pikachu1.jpeg
```

> To train a new model
```shell
$ python3 train.py --dataset path_to_dataset --model path_to_pokedex.model --labelbin lb.pickle
```

> For more details about the arguments
```
$ python3 classifier.py --help
```
```
$ python3 train.py --help
```
---

## Results

### Graphics

- This is the graphic of the first model that was trained.
 ![first model](https://github.com/thaynnara007/pokedex/blob/master/first_model_plot.png)

- This is the graphic of the last model that was trained; this one had a bigger dataset.
 ![last model](https://github.com/thaynnara007/pokedex/blob/master/last_model_plot.png)

---

### Classification

- Here there are some examples of successful images classification
- There are more examples of classification in examples package
- Pikachu
 ![pikachu](https://github.com/thaynnara007/pokedex/blob/master/examples/pikachu.png)
- Charmander
 ![charmander](https://github.com/thaynnara007/pokedex/blob/master/examples/charmander.png)
- Bulbasaur
 ![bulbasaur](https://github.com/thaynnara007/pokedex/blob/master/examples/bulbasaur.png)
- Squirtle
 ![squirtle](https://github.com/thaynnara007/pokedex/blob/master/examples/squirtle.png)
- Cyndaquil
 ![cyndaquil](https://github.com/thaynnara007/pokedex/blob/master/examples/cyndaquil2.png)
- Chikorita
 ![chikorita](https://github.com/thaynnara007/pokedex/blob/master/examples/chikorita.png)
- Totodile
 ![totodile](https://github.com/thaynnara007/pokedex/blob/master/examples/totodile.png)

---

## Built with

- [Keras](https://keras.io/)
- [Tensorflow](https://www.tensorflow.org/) as Keras backend
- [Sklearn](https://scikit-learn.org/stable/)
- [OpenCV](https://opencv.org/)

