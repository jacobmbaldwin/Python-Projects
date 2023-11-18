# HTML/CSS Product Card Generator
# By Jacob Baldwin
# 11/17/2023

# The purpose of this script is to first generate URL query parameters for tracking performance, then generate simple HTML/CSS product cards. The intended use-case is for blog articles on e-commerce platforms.
# All links on the cards automatically append the URL query parameter. It is not recommended to do more than 3 cards in a single cardWrapper.

# Generate URL query parameter
print("\033[1mFirst, let's generate the query parameter for your article:\033[0m\n")

mainCat = input('Enter the Main Category (no caps): ')
subCat = input('Enter the subcategory (no caps): ')
articleTitle = input('Enter the article title (No caps, No spaces - use "-" instead): ')

# Change "yourblog" to blog name
initialParam = '?cm_soc=yourblog&amp;type='

queryParam = (initialParam + mainCat + "|" + subCat + "|" + articleTitle)

print("\n\033[1mYour query parameter is:\033[0m ")
print(queryParam + "\n")

# Generate Product Cards
print("\033[1mNow, let's generate your product cards:\033[0m\n")

# Request input for how many cards you want to generate
card_count = int(input("Enter how many cards you need (1-3): "))

# Initialize the string that will contain the HTML code for "Cards"
cards = ""

# Loop to request card input data and output HTML/CSS
for i in range(card_count):
  category = input("Enter the product category name: ")
  categoryLink = input("Enter the product category link address: ")
  imageLink = input("Enter the product image link address: ")
  productTitle = input("Enter the product title: ")
  productDescription = input("Enter the product description: ")
  productLink = input("Enter the product link address: ")
  print("\n")

# Mapping the input variables for formatting the cards string
  inputs = {'cat':category, 'catLink':categoryLink, 'img':imageLink, 'prod':productTitle, 'prodDesc':productDescription, 'prodLink':productLink, 'query':queryParam}

# Append the HTML for each card in the loop into the cards string
  cards += '''
      <div class="cardContainer">
          <p class="smallTitle">
              <a
                  href="{catLink}{query}"
                  >{cat}</a
              >
          </p>
          <div class="imagesWrapper">
              <img
                  src="{img}"
                  alt="{prod}" />
          </div>
          <div class="productWrapper">
              <a
                  class="productTitle"
                  href="{prodLink}{query}"
                  target="_blank">
                  <h3 class="h3">
                      {prod}
                  </h3>
              </a>

              <p class="descP">
                  {prodDesc}
              </p>
              <a
                  href="{prodLink}{query}"
                  target="_blank"
                  class="add"
                  ><button class="add">Shop Now</button></a
              >
          </div>
      </div>
  '''.format(**inputs)

# String that contains the CSS for our cards
style = '''
  <style>
    .cardWrapper {
        display: flex;
        justify-content: center;
        align-items: stretch;
        gap: 2rem;
        padding-block: 3rem;
    }

    .cardContainer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: white;
        box-shadow: 5px 5px 15px grey;
        border-radius: 10px;
        flex-direction: column;
        padding: 1rem 0rem;
        position: relative;
        gap: 0.4rem;
        flex: 1;
    }

    .imagesWrapper {
        padding-top: 2rem;
        width: 200px;
        height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .imagesWrapper > img {
        width: 100%;
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }

    .productWrapper {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        text-align: center;
        width: 90%;
        gap: 0.5rem;
    }

    .smallTitle {
        font-size: 0.6em;
        letter-spacing: 1px;
        display: flex;
        justify-content: flex-start;
        text-transform: uppercase;
        margin: 0 !important;
        width: 100%;
        padding-left: 2rem;
        text-transform: uppercase;
    }

    .h3 {
        font-size: calc(39% + 1vw);
        line-height: calc(39% + 1vw);
    }

    .descP {
        text-transform: none;
        letter-spacing: 0;
        font-size: calc(31% + 0.5vw);
        line-height: calc(70% + 0.5vw);
        text-align: justify;
    }

    .add {
        width: 100%;
        margin-top: 0.5rem;
        border-bottom: none !important;
    }

    button {
        background: #213629;
        padding: 10px;
        display: inline-block;
        outline: 0;
        border: 0;
        margin: -1px;
        border-radius: 8px;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: white;
        cursor: pointer;
    }

    button:hover {
        background: green;
        color: white;
        transition: all 0.4s ease-in-out;
    }

    .productTitle {
        color: black !important;
        text-decoration: none !important;
        border-bottom: none !important;
    }

    .productTitle:hover > .h3 {
        color: #ad141e !important;
        transition: all 0.4s ease-in-out;
    }

    @media (max-width: 768px) {
        .add {
            width: 70%;
            margin-top: 0.5rem;
        }

        .cardWrapper {
            flex-direction: column;
        }

        .imagesWrapper > img {
            width: 100%;
            padding: 2rem 0rem;
        }

        .h3 {
            font-size: calc(80% + 2vw);
            line-height: calc(80% + 1vw);
        }

        .descP {
            text-transform: none;
            letter-spacing: 0;
            font-size: calc(30% + 1.5vw);
            line-height: calc(60% + 1.5vw);
        }
    }
  </style>
'''

# Output string for the HTML portion of our cards. Creates the overall wrapper and places the generated cards inside of the div.
output = '''
  <div class="cardWrapper">
    {}
  </div>
'''.format(''.join(cards))

# Output the HTML/CSS.
print("\033[1mYour HTML/CSS Product Cards:\033[0m ", style, output, sep="\n\n")
