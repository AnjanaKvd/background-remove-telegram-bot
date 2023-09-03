import requests

class RemoveBackgroundAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.remove.bg/v1.0/removebg'

    def remove_background(self, image_path, output_path='no-bg.png', size='auto'):
        files = {'image_file': open(image_path, 'rb')}
        data = {'size': size}
        headers = {'X-Api-Key': self.api_key}

        response = requests.post(
            self.api_url,
            files=files,
            data=data,
            headers=headers,
        )

        if response.status_code == requests.codes.ok:
            with open(output_path, 'wb') as out:
                out.write(response.content)
            print("Background removed successfully. Image saved as", output_path)
        else:
            print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    TOKEN = "Your remove bg api token"
    image_path = 'bg-remove.png'
    remove_bg_api = RemoveBackgroundAPI(TOKEN)
    remove_bg_api.remove_background(image_path)
