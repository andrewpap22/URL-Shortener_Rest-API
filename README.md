Software Engineer Task
======================

At Plum, we have a lot of services that need to work together to deliver our product.
Many of these services talk to third-party providers to perform their operations – for
example moving money, performing background checks, sending messages or emails, etc.

In a lot of cases - due to business, compliance or technical reasons - we need to support
multiple third-party providers for the same operation, some of which have wildy different
specifications, ranging from simple REST APIs to SOAP.

To maintain our sanity, we abstract these third-parties behind interfaces and expose
consistent APIs for the rest of the system to consume. Each service should be able to
pick sensible defaults (and fallbacks, if, for example, a provider is unavailable) or
allow the consumer to specify the provider if they wish to do so.

<hr>

## 📁 Project File Structure

<ul>
  <li>
    <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty">📂 shorty</a>
    <ul>
      <li>
        <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/custom_shorty">📂 custom_shorty</a>
        <ul>
          <li>
            <p>📄 custom.py</p>
          </li>
        </ul>
      </li>
      <li>
        <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/error_msgs">📂 error_msgs</a>
        <ul>
          <li>
            <p>📄 errors.py</p>
          </li>
        </ul>
      </li>
      <li>
        <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/providers">📂 providers</a>
        <ul>
          <li>
            <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/providers/bitly">📂 bitly</a>
            <ul>
              <li>
                <p>📄 bit_ly.py</p>
              </li>
            </ul>
          </li>
          <li>
            <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/providers/tinyurl">📂 tinyurl</a>
            <ul>
              <li>
                <p>📄 tinyurl_com.py</p>
              </li>
            </ul>
          </li>
          <li>
            <p>📄 provider_short.py</p>
          </li>
        </ul>
      </li>
      <li>
        <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/static">📂 static</a>
        <ul>
          <li>
            <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/static/css">📂 css</a>
            <ul>
              <li>
                <p>📄 swagger-ui.css</p>
              </li>
            </ul>
          </li>
          <li>
            <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/static/img">📂 img</a>
            <ul>
              <li>
                <p>📄 favicon-16x16.png</p>
              </li>
              <li>
                <p>📄 favicon-32x32.png</p>
              </li>
            </ul>
          </li>
          <li>
            <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/static/js">📂 js</a>
            <ul>
              <li>
                <p>📄 swagger-ui-bundle.js</p>
              </li>
              <li>
                <p>📄 swagger-ui-standalone-preset.js</p>
              </li>
              <li>
                <p>📄 swagger-ui.js</p>
              </li>
            </ul>
          </li>
          <li>
            <p>📄 openapi2.json</p>
          </li>
        </ul>
      </li>
      <li>
        <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/shorty/templates">📂 templates</a>
        <ul>
          <li>
            <p>📄 swaggerui.html</p>
          </li>
        </ul>
      </li>
      <li>
        <p>📄 api.py</p>
      </li>
      <li>
        <p>📄 app.py</p>
      </li>
    </ul>
  </li>
  <li>
    <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/tests">📂 tests</a>
    <ul>
      <li>
        <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/tests/functional_tests">📂 functional_tests</a>
        <ul>
          <li>
            <p>📄 conftest.py</p>
          </li>
          <li>
            <p>📄 test_shorty_api.py</p>
          </li>
        </ul>
      </li>
      <li>
        <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/tests/unit_tests">📂 unit_tests</a>
        <ul>
          <li>
            <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/tests/unit_tests/test_custom_shorty">📂 test_custom_shorty</a>
            <ul>
              <li>
                <p>📄 test_custom.py</p>
              </li>
            </ul>
          </li>
          <li>
            <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/tests/unit_tests/test_providers">📂 test_providers</a>
            <ul>
              <li>
                <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/tests/unit_tests/test_providers/test_bitly">📂 test_bitly</a>
                <ul>
                  <li>
                    <p>📄 test_bit_ly.py</p>
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://github.com/andrewpap22/Plum_Software-Engineer-Task/tree/shorty/tests/unit_tests/test_providers/test_tinyurl">📂 test_tinyurl</a>
                <ul>
                  <li>
                    <p>📄 test_tinyurl_com.py</p>
                  </li>
                </ul>
              </li>
              <li>
                <p>📄 test_provider_short.py</p>
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  <li><p>🐳 Dockerfile</p></li>
  <li><p>📄 LICENSE</p></li>
  <li><p>📄 README.md</p></li>
  <li><p>📄 requirements.txt</p></li>
  <li><p>📄 run.py</p></li>
  <li><p>💾 virtual_enviroment.sh</p></li>
  </li>
</ul>

<hr>

Mission
-------

Your mission, should you choose to accept it, is to build a microservice called `shorty`, 
which supports two URL shortening providers: [bit.ly](https://dev.bitly.com/) and [tinyurl.com](https://gist.github.com/MikeRogers0/2907534).
You don't need to actually sign up to these providers, just implement their API. The
service exposes a single endpoint: `POST /shortlinks`. The endpoint should receive
JSON with the following schema:

| param    | type   | required | description                        |
|----------|--------|----------|------------------------------------|
| url      | string | Y        | The URL to shorten                 |
| provider | string | N        | The provider to use for shortening |

The response should be a `Shortlink` resource containing:

| param    | type   | required | description                        |
|----------|--------|----------|------------------------------------|
| url      | string | Y        | The original URL                   |
| link     | string | Y        | The shortened link                 |

For example:
```json
{
    "url": "https://example.com",
    "link": "https://bit.ly/8h1bka"
}
```

You are free to decide how to pick between the providers if one is not requested and what
your fallback strategy is in case your primary choice fails. Your endpoint needs to return
a JSON response with a sensible HTTP status in case of errors or failures.

<hr>

## Details ✍️

So, `shorty` shortens the url given as a request using as a `default` provider the **tinyurl** provider. If the user decides to choose the provider though he's free to do so, and if both providers are unavailable for any reason, shorty uses a custom built in short() function to shorten the url requested. <br>
`Example:`

```json
{
  "url":"https://www.example.com/",
  "provider":"bitly"
}
```

`Shorty` checks for every possible mistake the user might do and provides a useful message for the user alongside an appropriate HTTP status code. <br>
`An example of a possible error message:`

```json
{
    "Error": "[!] Request must be provided in json format.",
    "Usage": [
        {
          "url":"https://www.example.com/",
          "provider":"bitly"
        },
        {
            "url":"http://example.com/",
            "provider":"tinyurl"
        },
        {
            "url":"http://example.com"
        }
    ]
}
```

After all `shorty` responds back if everything's ok. <br>
`Response Example`

```json
{
    "url": "https://example.com",
    "link": "https://bit.ly/8h1bka"
}
```

<hr>

What you need to do
-------------------

1. Create a Python env (using Python 3.6+) and install the requirements.
2. Build the `POST /shortlinks` endpoint. We've provided a skeleton API using `flask`.
3. Write some tests. We've provided a test blueprint using `pytest`.

Deliverable
-----------

You should deliver your solution as a Pull Request in your repo. Document your design choices and anything else you think we need to know in the PR description.

What we look for
----------------

In a nutshell, we're looking for tidy, production-quality code, a scalable design and sensible
tests (unit tests, integration tests or both?). Imagine that your code will be read by other 
developers in your team – keep them happy :-)

Resources
---------

1. `Flask`: http://flask.pocoo.org/
2. `pytest`: http://pytest.org/latest/
3. `virtualenvwrapper`: https://virtualenvwrapper.readthedocs.io/en/latest/
4. `HTTP statuses`: https://httpstatuses.com/

Disclaimer
----------

We will not use any of this code for any of Plum's applications.
