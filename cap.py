import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import easyocr
import time

# Mengarahkan pesan CUDA ke stdout yang kosong
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Inisialisasi driver Chrome
driver = webdriver.Chrome()

# Inisialisasi pembaca EasyOCR dengan bahasa tertentu
reader = easyocr.Reader(['en'])

def meter():
    try:
        #Pilih Aset meter
        asset_type = driver.find_element(By. XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]")
        asset_type.click()
        meter_type = driver.find_element (By. XPATH, "/html/body/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div")
        meter_type.click()

        time.sleep(1)

        asset_code = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div/input")
        asset_code.send_keys("217066407")

        time.sleep(2)

        brand = driver.find_element(By. XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[4]/div/div/div/div/div/div/div[2]/div")
        brand.click()

        edmi_type = driver.find_element (By. XPATH, "/html/body/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div")
        edmi_type.click()
        time.sleep(2)

        brand_type = driver.find_element (By. XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[5]/div/div/div/div/div/div/div[2]/div")
        brand_type.click()

        mke = driver.find_element (By. XPATH, "/html/body/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div")
        mke.click()
        time.sleep(4)

        save = driver.find_element (By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/div[1]/div[3]/dx-button")
        save.click()
        time.sleep(2)

        #yes = driver.find_element (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/dx-button[2]")
        #yes.click()

        time.sleep(30)


    except Exception as e:     
        raise Exception(f"Terjadi error saat mengisi form: {str(e)}")


def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

def modem():
    try:
        assett_type = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]")
        assett_type.click()

        modem_type = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div")
        modem_type.click()

        time.sleep(1)

        assett_code = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div/input")
        assett_code.send_keys("867018061016501")
        time.sleep(2)

        brandd = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[4]/div/div/div/div/div/div/div[2]/div")
        brandd.click()


        elip_type = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[13]/div")
        scroll_to_element(driver, elip_type)  # Scroll ke elemen 'elip_type' terlebih dahulu
        elip_type.click()
        time.sleep(2)

        brandd_type = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[5]/div/div/div/div/div/div/div[2]/div")
        brandd_type.click()

        
        NG = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div/div")
        NG.click()
        time.sleep(4)

        save = driver.find_element (By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/div[1]/div[3]/dx-button")
        save.click()
        time.sleep(20)

        #yes = driver.find_element (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/dx-button[2]")
        #yes.click()

    except Exception as e:
        raise Exception(f"Terjadi error saat mengisi form: {str(e)}")


def sim():
    try:

        assettt_type = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]")
        assettt_type.click()        
        sim_type = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[4]/div")
        sim_type.click()

        time.sleep(1)

        assettt_code = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div/input")
        assettt_code.send_keys("867018061016501")
        time.sleep(2)

        branddd = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[4]/div/div/div/div/div/div/div[2]/div")
        branddd.click()

        tel_type = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div")
        tel_type.click()
        time.sleep(2)
        # Asumsikan element yang akan diinteraksi dengan IP adalah 'element'


        IP = driver.find_element(By.NAME, "dynamicData.IP.attributeValue")
        #IP = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/dx-form/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/input")
        #IP.getText()
        #element.click()
        IP.send_keys("12344")
        time.sleep(2)


        driver.execute_script("window.scrollTo(0, 0);")

        time.sleep(2)




        save = driver.find_element (By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div[2]/app-asset-edit/div/div/div[2]/form/div[1]/div[3]/dx-button")
        save.click()
        time.sleep(10)


        #yes = driver.find_element (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/dx-button[2]")
        #yes.click()


    except Exception as e:
        raise Exception(f"Terjadi error saat mengisi form: {str(e)}")

# Fungsi untuk membaca CAPTCHA
def read_captcha():
    try:
        # Tangkap gambar CAPTCHA
        captcha_element = driver.find_element(By.XPATH, "/html/body/app-dashboard/ng-component/div/div/div/div/div[2]/form/div[4]/canvas")
        screenshot_path = "captcha.png"
        captcha_element.screenshot(screenshot_path)

        # Menggunakan EasyOCR untuk membaca teks dari gambar CAPTCHA
        results = reader.readtext(screenshot_path)

        if not results:
            raise Exception("Gagal membaca teks CAPTCHA")

        captcha_text = results[0][1]

        return captcha_text

    except Exception as e:
        raise Exception(f"Terjadi error saat membaca CAPTCHA: {str(e)}")

try:
    # Buka URL target
    driver.get("https://amicon.pln.co.id/#/pages/login?returnUrl=%2Fdashboard_technical")


    # Mengabaikan peringatan keamanan (SSL)
    keamanan = driver.find_element(By.ID, "details-button")
    keamanan.click()
    lanjut = driver.find_element(By.ID, "proceed-link")
    lanjut.click()



    # Tunggu beberapa saat untuk memastikan halaman telah terbuka
    time.sleep(3)

    # Isi formulir login
    driver.find_element(By.XPATH, "/html/body/app-dashboard/ng-component/div/div/div/div/div[2]/form/div[2]/input").send_keys("pusat\\asdar02")
    driver.find_element(By.XPATH, "/html/body/app-dashboard/ng-component/div/div/div/div/div[2]/form/div[3]/input").send_keys("9615040-a37")

    time.sleep(5)
    while True:
        try:
            start_time = time.time()  # Catat waktu awal

            captcha_text = read_captcha()

            # Isi teks CAPTCHA ke dalam formulir CAPTCHA
            captcha_input_element = driver.find_element(By.XPATH, "/html/body/app-dashboard/ng-component/div/div/div/div/div[2]/form/div[5]/input")
            captcha_input_element.send_keys(captcha_text)

            # Klik tombol login
            login_button_element = driver.find_element(By.XPATH, "/html/body/app-dashboard/ng-component/div/div/div/div/div[3]/button")
            login_button_element.click()

            # Tunggu hingga proses selesai
            elapsed_time = time.time() - start_time
            time.sleep(max(0, 5 - elapsed_time))  # Tunggu selama 5 detik setelah mengurangi waktu yang sudah berlalu

            # Jika berhasil login, memilih menu "asset"
            if "dashboard" in driver.current_url:
                # Memilih menu "asset"
                asset_menu_element = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/div/nav/ul/li[2]/a")
                asset_menu_element.click()

                time.sleep(2)

                # Menunggu hingga halaman "asset" terbuka
                if "asset" in driver.current_url:
                    # Menemukan tombol "New Asset" dan menekannya
                    new_asset_button = driver.find_element(By.XPATH, "/html/body/app-dashboard/div/main/div/app-site/div/div/div/div[2]/div/dx-data-grid/div/div[4]/div/div/div[1]/div/div/div/div")
                    new_asset_button.click()

                    time.sleep(2)
                    sim()

                    time.sleep(3)

        except Exception as e:
            error_message = f"Terjadi error: {str(e)}"
            print(error_message)

            captcha_input_element = driver.find_element(By.XPATH, "/html/body/app-dashboard/ng-component/div/div/div/div/div[2]/form/div[5]/input")
            captcha_input_element.clear()

            time.sleep(3)

            # Jika gagal membaca CAPTCHA, tekan tombol refresh CAPTCHA
            refresh_captcha_button = driver.find_element(By.XPATH, "/html/body/app-dashboard/ng-component/div/div/div/div/div[2]/form/div[4]/button")
            refresh_captcha_button.click()


            # Tunggu sebentar sebelum mencoba lagi (Anda dapat mengubahnya sesuai kebutuhan)
            time.sleep(3)

except Exception as e:
    error_message = f"Terjadi error: {str(e)}"
    print(error_message)

finally:
    # Tutup driver
    driver.quit()