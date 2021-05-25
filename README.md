# restaurant-chatbot

## Introduction

This repository contains the code for a simple chatbot capable of handling reservation of seats for a restaurant. The framework used for this project is  [Rasa](https://rasa.com/docs/rasa/).

## Description

The chatbot is designed using an open source machine learning framework `Rasa`. It makes use of `Rasa forms` to extract and store required booking information from the user. The user is asked to provide the time of booking, no. of seats and section (`AC` / `Non-AC`). The extracted entities are parsed according to defined user intents and the values are stored in appropriate slots. The form actiavtes a loop which keeps on asking the user for the required entities till all slots are filled. The bot is also capable of handling chitchats and answering frequently asked questions (FAQs) in the midst of extracting information from the user. To extract time from user input, [Duckling Entity Extractor](https://github.com/facebook/duckling) has been used. The time is extracted from the date-time object and the action module has been used to handle time validation logic which automatically rejects any booking time outside the allowed time (7pm - 10pm).

## Installation

In order to install and use the chatbot, A `LINUX` environment is required with `python3` already installed.

1.  Install `Rasa Open Source` in a fresh virtual environment `venv` by running the `setup.py` file:
    ```
    $ python3 setup.py
    ```
    You can refer to [Rasa Installation guide](https://rasa.com/docs/rasa/user-guide/installation/) for more details related to installing `Rasa`.

2. To extract time from user input, install `Duckling`:
    ```
    $ wget -qO- https://get.haskellstack.org/ | sh
    $ sudo apt-get install libpcre3 libpcre3-dev
    $ git clone https://github.com/facebook/duckling.git
    $ cd duckling
    $ stack build
    ```

## Usage

1. To run the `Duckling` server:
    ```
    $ cd duckling
    $ stack exec duckling-example-exe
    ```

2. To run the action server:
    ```
    $ . ./venv/bin/activate
    $ python -m rasa_sdk.endpoint --actions actions
    ```

3. To start the chatbot in command line interface, run:
    ```
    $ . ./venv/bin/activate
    $ rasa shell --endpoints endpoints.yml
    ```

## Supported FAQs

    1. Working days of the restaurant
    2. Timings of the restaurant
    3. Reservation cancellation procedure
    4. Special dishes
