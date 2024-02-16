import requests


#დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის 
#გამოყენებით "https://fakestoreapi.com/products" მისამართზე, შეამოწმებს სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:
def get_products():
    try:
        api_url = "https://fakestoreapi.com/products"
        response = requests.get(api_url)

        print(response.status_code, "\n")

        if response.status_code != 200:
            print(f"ERROR: can't get data. Status {response.status_code}")
            return False

        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"ERROR: {http_err}")
    except requests.exceptions.ConnectionError as con_err:
        print(f"Connection error: {con_err}")
    except Exception as err:
        print(f"Something wrong! {err}")

#ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები

def parse_data():
    products = get_products()

    if not products:
        return

    products_prices = [product['price'] for product in products]

    print(products_prices)
    
    min_price = min(products_prices)
    max_price = max(products_prices)

    print(f"Minimum Price: {min_price}")
    print(f"Maximum Price: {max_price}")


parse_data()

#ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ
        
def parse_data():
    products = get_products()

    if not products:
        return
    
    categories = list(set(product['category'] for product in products))
   
    sorted_categories = sorted(categories)

    print(sorted_categories)

parse_data()

#გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
def parse_data():
    products = get_products()

    if not products:
        return

    title_and_id = [{'id': product['id'], 'title': product['title']} for product in products]

    sorted_title_and_id = sorted(title_and_id, key=lambda x: x['title'])

    print(sorted_title_and_id)

parse_data()
#დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით
def parse_data():
    products = get_products()

    if not products:
        return

    ratings = [product['rating'] for product in products]
    sorted_data = sorted(ratings, key=lambda x: x['rate'])
    
    print(sorted_data)
parse_data()