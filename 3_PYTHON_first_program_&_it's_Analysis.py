{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "##First Python program\n",
        "#####There is a common practice of printing \"Hellow world\" whenever someone starts his/her first programming language, no matter what ever language it is, JAVA, Python or C++.\n",
        "printing \"Hello world\" is the easiest task in python programming out of all other languages. so let us do it."
      ],
      "metadata": {
        "id": "AHGOFlKPUNcR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print (\"Hello World\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8in8UbJSbq3z",
        "outputId": "e756edb1-849b-41f9-bd10-9851888fe46a"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "####Analsis of above code:\n",
        "In the above code, print(\"Hello world\"), things we are understanding is that, \n",
        "\n",
        "#####-In python programming, to print anything you have to use the command print with parentheses in this way: print(). And insinde the parentheses we have to write the command that we need to print.\n",
        "#####-Python is a case sensetive language therefor \"print\" , \"Print\" and \"PRINT\" are all three different words for python and hence writing \"Print\" in place of  \"print\" will give an error to us. We have to always use lowercase letters to write the print statement\n",
        "#####-After writing print, inside the parentheses we can withe the things we want to print. In python, if we want to print a statement as it is, we have to use ellipsis(\"\"), this will print the lines as it is inside the ellipsis \n"
      ],
      "metadata": {
        "id": "DM1rMQ-IcRox"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(Hello world)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 134
        },
        "id": "FfKnqG4TcUG1",
        "outputId": "b5d62a89-1c6d-4a88-a02e-7df6092efcbe"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-4-50b4ae29d403>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    print(Hello world)\u001b[0m\n\u001b[0m                ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#####As elipsis is not used here, python is taking hello worls as any of his inbuilt code but cannot find any such code inside it, and shows error."
      ],
      "metadata": {
        "id": "_hL5MuH6fDhN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(5+10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ABQ-uuBAfuhy",
        "outputId": "dcb89cac-e0c3-45b4-c6a9-a3469f152bc2"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "You can also use print function to print arithmetic calculations of numbers as shown above."
      ],
      "metadata": {
        "id": "wZ9-OMLMf0Id"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Substracting 5 from 10 will give: \" , 10-5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YCxd3hlBgHU4",
        "outputId": "fdfe99f2-90a3-4bea-d99f-be0fc0001404"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Substracting 5 from 10 will give:  5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "I can use both elipsis and arithmetic calculations to make my output more understandable.\n",
        "I have seperated both of the outputs using a comma(,) "
      ],
      "metadata": {
        "id": "vdDr2bpjgbiM"
      }
    }
  ]
}