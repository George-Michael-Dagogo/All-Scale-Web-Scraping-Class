# All-Scale-Web-Scraping-Class





### **Window and Display Options**

* `--start-maximized`: Launches the browser in a maximized window.
* `--window-size=width,height`: Sets the initial window size, e.g., `--window-size=1280,800`.
* `--window-position=x,y`: Sets the initial window position on the screen.
* `--start-fullscreen`: Launches the browser in full-screen mode.
* `--kiosk`: Launches Chrome in kiosk mode (full-screen without browser UI).
* `--headless`: Runs Chrome in headless mode (no GUI), useful for automated testing.
* `--disable-gpu`: Disables GPU hardware acceleration; often used with headless mode.
* `--force-device-scale-factor=1.25`: Forces a device scale factor; useful for high-DPI displays.
* `--high-dpi-support=1`: Enables high-DPI support.

---

### **User Profile and Session Management**

* `--user-data-dir=path`: Specifies the user data directory, allowing the use of a custom profile.
* `--profile-directory=Default`: Specifies the profile directory within the user data directory.
* `--incognito`: Launches Chrome in incognito mode.
* `--no-first-run`: Skips the first-run tasks, such as the welcome page.
* `--disable-extensions`: Disables all Chrome extensions.

---

### **Security and Privacy**

* `--disable-web-security`: Disables the same-origin policy; useful for testing but not recommended for production.
* `--allow-running-insecure-content`: Allows loading of insecure content (HTTP) on secure pages (HTTPS).
* `--ignore-certificate-errors`: Ignores SSL certificate errors.
* `--disable-popup-blocking`: Disables the popup blocking feature.

---

### **Performance and Behavior**

* `--disable-plugins`: Disables all plugins.
* `--disable-infobars`: Prevents Chrome from displaying the "Chrome is being controlled by automated test software" infobar.
* `--disable-notifications`: Disables web notifications.
* `--disable-translate`: Disables the translation feature.
* `--no-sandbox`: Disables the sandbox for all process types; use with caution.
* `--disable-dev-shm-usage`: Writes shared memory files into `/tmp` instead of `/dev/shm`; useful in Docker environments.

---

### **Networking**

* `--proxy-server=host:port`: Specifies the proxy server to use.
* `--proxy-bypass-list=hosts`: Specifies a list of hosts to bypass the proxy.
* `--host-resolver-rules=rules`: Specifies rules for host name resolution.

---

### **Logging and Debugging**

* `--enable-logging`: Enables logging.
* `--v=level`: Sets the logging verbosity level.
* `--log-path=path`: Specifies the file path for logging.

---

### **Experimental and Advanced Options**

* `--remote-debugging-port=port`: Enables remote debugging on the specified port.
* `--disable-features=FeatureName`: Disables specific Chrome features.
* `--enable-features=FeatureName`: Enables specific Chrome features.
* `--load-extension=path`: Loads a Chrome extension from the specified path.

---

Please note that while these options can be set using `add_argument()` in Selenium's ChromeOptions, not all options are compatible with every Chrome version or environment. Always test configurations in your specific setup.

