# Nanopy
Official CLI app for NBlog.

## Installation
Make sure you have Python installed in PATH.

Open your terminal and type `pip install -r requirements.txt`.

## Usage

## Posting
```sh
python nano.py post https://localhost "wow"
```

If you want to cross-post to [imood.com](https://imood.com), type this instead:

```sh
python nano.py post https://localhost "wow" --imood="true"
```

## Reading
```sh
python nano.py read https://localhost
```

## Editing
```sh
python nano.py edit https://localhost "edit" 1
```

## Deleting
```
python nano.py delete https://localhost 1
```
