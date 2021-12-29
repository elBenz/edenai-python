# coding: utf-8

"""
    Eden AI API Documentation

    <a href=\"https://app.edenai.run/user/login\" target=\"_blank\"><img src=\"/static/images/welcome.png\"></a>. # Welcome  Eden AI simplifies the use and integration of AI technologies by providing a unique API connected to the best AI engines and combined with a powerful management platform. The platform covers a wide range of AI technologies: * Vision:  <a href=\"https://www.edenai.co/vision\" target=\"_blank\">www.edenai.co/vision</a>. * Text & NLP: <a href=\"https://www.edenai.co/text\" target=\"_blank\">www.edenai.co/text</a>. * Speech & Audio: <a href=\"https://www.edenai.co/speech\" target=\"_blank\">www.edenai.co/speech</a>. * OCR: <a href=\"https://www.edenai.co/ocr\" target=\"_blank\">www.edenai.co/ocr</a>. * Machine Translation: <a href=\"https://www.edenai.co/translation\" target=\"_blank\">www.edenai.co/translation</a>. * Prediction: <a href=\"https://www.edenai.co/prediction\" target=\"_blank\">www.edenai.co/prediction</a>.  For all the proposed technologies, we provide a single endpoint:  the service provider is only a parameter that can be changed very easily. All the engines available on Eden AI are listed here: www.edenai.co/catalog  # Support & community  ### 1- Support If you have any problems, please contact us at this email address: contact@edenai.co. We will be happy to help you in the use of Eden AI.   ### 2- Community  You can interact personally with other people actively using and working with Eden AI and join our  <a href=\"https://join.slack.com/t/edenai/shared_invite/zt-t68c2pr9-4lDKQ_qEqmLiWNptQzB_6w\" target=\"_blank\">Slack community</a>.  We are always updating our docs, so a good way to always stay up to date is to watch our documentation repo on Github: <a href=\"https://github.com/edenai\" target=\"_blank\">https://github.com/edenai</a>.  ### 3- Blog  We also regularly publish various articles with Eden AI news and technical articles on the different AI engines that exist. You can find these articles here: <a href=\"https://www.edenai.co/blog\" target=\"_blank\">https://www.edenai.co/blog</a>.   # Authentication  ## Create account ![Register](/static/images/register.png)  To create an account, please go to this link: <a href=\"https://app.edenai.run/user/login\" target=\"_blank\">app.edenai.run/user/login</a>. You can create an account with your email address or by using your account on available platforms (Gmail, Github, etc.).   By creating an account with your email address, you will receive a confirmation email with a link to click. Check your spam if needed and contact us if you have any problem: contact@edenai.co  ![Login](/static/images/login.png) ## API key  By going to your account page on the platform: <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">https://app.edenai.run/admin/account</a>, you will have access to your API key to start using the different AI engines offered by Eden AI.   ![api_key](/static/images/api_key.png) # Portal Guide  Eden AI provides a web portal that allows you to do several tasks:  ![portal](/static/images/portal.png)  ### 1- Benchmark and test The platform allows you to easily compare competing engines without having to code. By uploading your data, you have access to the prediction results of the different engines. This gives you a first overview of the performance of AI engines.   ![benchmark](/static/images/benchmark.png)  ### 2- Cost management The <a href=\"https://app.edenai.run/admin/cost-management\" target=\"_blank\">cost management page</a> also allows you to centralize the costs associated with the different engines with various filters to simplify the analysis.   This page also allows you to define monthly budget limits not to be exceeded to secure the use of different AI engines.   ![cost-management](/static/images/cost_management.png) ### 3- Account The <a href=\"https://app.edenai.run/admin/account\" target=\"_blank\">account page</a> allows you to change your information and password. It also gives you access to your API key that you can renew if needed.   This page also allows you to add a credit card and to buy with credits to use all the engines offered by Eden AI.   ![account](/static/images/account.png)   # API Guide  Eden AI API has different endpoints that refer to different AI services. The connected providers are thus parameters that the user can easily change.   # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@edenai.co
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from edenai.api_client import ApiClient


class TranslationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def automatic_translation(self, text, source_language, target_language, providers, **kwargs):  # noqa: E501
        """automatic_translation  # noqa: E501

        Machine translation refers to the translation of a text into another language using rules, statics or ml technics.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |---------------------------|-------------------------------|---------------|  | **Afrikaans**             | *`string`* | `af-AF`         |  | **Albanian**              | *`string`* | `sq-SQ`         |  | **Amharic**               | *`string`* | `am-AM`         |  | **Arabic**                | *`string`* | `ar-XA`         |  | **Armenian**              | *`string`* | `hy-HY`         |  | **Azerbaijani**           | *`string`* | `az-AZ`         |  | **Basque**                | *`string`* | `eu-BA`         |  | **Belarusian**            | *`string`* | `be-BE`         |  | **Bengali**               | *`string`* | `bn-BN`         |  | **Bosnian**               | *`string`* | `bs-BS`         |  | **Bulgarian**             | *`string`* | `bg-BG`         |  | **Catalan**               | *`string`* | `ca-ES`         |  | **Cebuano**               | *`string`* | `ceb-CB`        |  | **Chinese-Simplified**    | *`string`* | `zh-CN`         |  | **Chinese-Traditional**   | *`string`* | `zh-TW`         |  | **Corsican**              | *`string`* | `co-CO`         |  | **Croatian**              | *`string`* | `hr-HR`         |  | **Czech**                 | *`string`* | `cz-CZ`         |  | **Danish**                | *`string`* | `da-DK`         |  | **Dutch**                 | *`string`* | `nl-NL`         |  | **English**               | *`string`* | `en-US`         |  | **Esperanto**             | *`string`* | `eo-EO`         |  | **Estonian**              | *`string`* | `et-ET`         |  | **Finnish**               | *`string`* | `fn-FN`         |  | **French**                | *`string`* | `fr-FR`         |  | **French-Canadian**       | *`string`* | `fr-CA`      |  | **Frisian**               | *`string`* | `fy-FY`         |  | **Galician**              | *`string`* | `gl-GL`         |  | **Georgian**              | *`string`* | `ka-KA`         |  | **German**                | *`string`* | `de-DE`         |  | **Greek**                 | *`string`* | `gr-GR`         |  | **Gujarati**              | *`string`* | `gu-GU`         |  | **Haitian-Creole**        | *`string`* | `ht-HT`         |  | **Hausa**                 | *`string`* | `ha-HA`         |  | **Hawaiian**              | *`string`* | `haw-HA`        |  | **Hebrew**                | *`string`* | `he-HE`         |  | **Hindi**                 | *`string`* | `hi-HI`         |  | **Hmong**                 | *`string`* | `hmn_HM`        |  | **Hungarian**             | *`string`* | `hu-HU`         |  | **Icelandic**             | *`string`* | `is-IS`         |  | **Igbo**                  | *`string`* | `ig-IG`         |  | **Indonesian**            | *`string`* | `id-ID`         |  | **Irish**                 | *`string`* | `ga-IR`         |  | **Italian**               | *`string`* | `it-IT`         |  | **Japanese**              | *`string`* | `ja-JP`         |  | **Javanese**              | *`string`* | `jv-JV`         |  | **Kannada**               | *`string`* | `kn-KN`         |  | **Kazakh**                | *`string`* | `kk-KK`         |  | **Khmer**                 | *`string`* | `km-KM`         |  | **Korean**                | *`string`* | `ko-KR`         |  | **Kurdish**               | *`string`* | `ku-KU`         |  | **Kyrgyz**                | *`string`* | `ky-KY`         |  | **Lao**                   | *`string`* | `lo-LO`         |  | **Latin**                 | *`string`* | `la-LA`         |  | **Latvian**               | *`string`* | `lv-LV`         |  | **Lithuanian**            | *`string`* | `lt-LT`         |  | **Luxembourgish**         | *`string`* | `lb-LB`         |  | **Macedonian**            | *`string`* | `mk-MK`         |  | **Malagasy**              | *`string`* | `mg-MG`         |  | **Malay**                 | *`string`* | `ms-MY`         |  | **Malayalam**             | *`string`* | `ml-ML`         |  | **Maltese**               | *`string`* | `mt-MT`         |  | **Maori**                 | *`string`* | `mi-MI`         |  | **Marathi**               | *`string`* | `mr-MR`         |  | **Mongolian**             | *`string`* | `mn-MN`         |  | **Myanmar-Burmese**       | *`string`* | `my-MY`         |  | **Nepali**                | *`string`* | `ne-NE`         |  | **Norwegian**             | *`string`* | `no-NO`         |  | **Nyanja Chichewa**       | *`string`* | `ny-NY`         |  | **Pashto**                | *`string`* | `ps-PS`         |  | **Persian**               | *`string`* | `fa-FA`         |  | **Polish**                | *`string`* | `pl-PO`         |  | **Portuguese**            | *`string`* | `pt-PT`         |  | **Punjabi**               | *`string`* | `pa-PA`         |  | **Romanian**              | *`string`* | `ro-RO`         |  | **Russian**               | *`string`* | `ru-RU`         |  | **Samoan**                | *`string`* | `sm-SM`         |  | **Scots Gaelic**          | *`string`* | `gd-GD`         |  | **Serbian**               | *`string`* | `sr-SR`         |  | **Sesotho**               | *`string`* | `st-ST`         |  | **Shona**                 | *`string`* | `sn-SN`         |  | **Sindhi**                | *`string`* | `sd-SD`         |  | **Sinhala-Sinhalese**     | *`string`* | `si-SI`         |  | **Slovak**                | *`string`* | `sk-SK`         |  | **Slovenian**             | *`string`* | `sl-SL`         |  | **Somali**                | *`string`* | `so-SO`         |  | **Spanish**               | *`string`* | `es-ES`         |  | **Sundanese**             | *`string`* | `su-SU`         |  | **Swahili**               | *`string`* | `sh-SH`         |  | **Swedish**               | *`string`* | `sw-SW`         |  | **Tagalog-Filipino**      | *`string`* | `tl-TL`         |  | **Tajik**                 | *`string`* | `tg-TG`         |  | **Tamil**                 | *`string`* | `ta-TA`         |  | **Telugu**                | *`string`* | `te-TE`         |  | **Thai**                  | *`string`* | `th-TH`         |  | **Turkish**               | *`string`* | `tr-TR`         |  | **Ukrainian**             | *`string`* | `uk-UK`         |  | **Urdu**                  | *`string`* | `ur-UR`         |  | **Uzbek**                 | *`string`* | `uz-UZ`         |  | **Vietnamese**            | *`string`* | `vi-VI`         |  | **Welsh**                 | *`string`* | `cy-CY`         |  | **Xhosa**                 | *`string`* | `xh-XH`         |  | **Yiddish**               | *`string`* | `yi-YI`         |  | **Yoruba**                | *`string`* | `yo-YO`         |    **AVAILABLE PROVIDERS**  |Name|Value| |-------------------------------|---------------| | [**IBM Watson**](https://www.edenai.co/catalog/watson-language-translator)|`ibm`|                         |[**Google Cloud Services**](https://www.edenai.co/catalog/google-cloud-translation)|`google`|                         |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-translate)|`amazon`|                         |[**Micrososft Azure**](https://www.edenai.co/catalog/azure-translator)|`microsoft`|    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_translation(text, source_language, target_language, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text: (required)
        :param str source_language: (required)
        :param str target_language: (required)
        :param str providers: (required)
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.automatic_translation_with_http_info(text, source_language, target_language, providers, **kwargs)  # noqa: E501
        else:
            (data) = self.automatic_translation_with_http_info(text, source_language, target_language, providers, **kwargs)  # noqa: E501
            return data

    def automatic_translation_with_http_info(self, text, source_language, target_language, providers, **kwargs):  # noqa: E501
        """automatic_translation  # noqa: E501

        Machine translation refers to the translation of a text into another language using rules, statics or ml technics.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |---------------------------|-------------------------------|---------------|  | **Afrikaans**             | *`string`* | `af-AF`         |  | **Albanian**              | *`string`* | `sq-SQ`         |  | **Amharic**               | *`string`* | `am-AM`         |  | **Arabic**                | *`string`* | `ar-XA`         |  | **Armenian**              | *`string`* | `hy-HY`         |  | **Azerbaijani**           | *`string`* | `az-AZ`         |  | **Basque**                | *`string`* | `eu-BA`         |  | **Belarusian**            | *`string`* | `be-BE`         |  | **Bengali**               | *`string`* | `bn-BN`         |  | **Bosnian**               | *`string`* | `bs-BS`         |  | **Bulgarian**             | *`string`* | `bg-BG`         |  | **Catalan**               | *`string`* | `ca-ES`         |  | **Cebuano**               | *`string`* | `ceb-CB`        |  | **Chinese-Simplified**    | *`string`* | `zh-CN`         |  | **Chinese-Traditional**   | *`string`* | `zh-TW`         |  | **Corsican**              | *`string`* | `co-CO`         |  | **Croatian**              | *`string`* | `hr-HR`         |  | **Czech**                 | *`string`* | `cz-CZ`         |  | **Danish**                | *`string`* | `da-DK`         |  | **Dutch**                 | *`string`* | `nl-NL`         |  | **English**               | *`string`* | `en-US`         |  | **Esperanto**             | *`string`* | `eo-EO`         |  | **Estonian**              | *`string`* | `et-ET`         |  | **Finnish**               | *`string`* | `fn-FN`         |  | **French**                | *`string`* | `fr-FR`         |  | **French-Canadian**       | *`string`* | `fr-CA`      |  | **Frisian**               | *`string`* | `fy-FY`         |  | **Galician**              | *`string`* | `gl-GL`         |  | **Georgian**              | *`string`* | `ka-KA`         |  | **German**                | *`string`* | `de-DE`         |  | **Greek**                 | *`string`* | `gr-GR`         |  | **Gujarati**              | *`string`* | `gu-GU`         |  | **Haitian-Creole**        | *`string`* | `ht-HT`         |  | **Hausa**                 | *`string`* | `ha-HA`         |  | **Hawaiian**              | *`string`* | `haw-HA`        |  | **Hebrew**                | *`string`* | `he-HE`         |  | **Hindi**                 | *`string`* | `hi-HI`         |  | **Hmong**                 | *`string`* | `hmn_HM`        |  | **Hungarian**             | *`string`* | `hu-HU`         |  | **Icelandic**             | *`string`* | `is-IS`         |  | **Igbo**                  | *`string`* | `ig-IG`         |  | **Indonesian**            | *`string`* | `id-ID`         |  | **Irish**                 | *`string`* | `ga-IR`         |  | **Italian**               | *`string`* | `it-IT`         |  | **Japanese**              | *`string`* | `ja-JP`         |  | **Javanese**              | *`string`* | `jv-JV`         |  | **Kannada**               | *`string`* | `kn-KN`         |  | **Kazakh**                | *`string`* | `kk-KK`         |  | **Khmer**                 | *`string`* | `km-KM`         |  | **Korean**                | *`string`* | `ko-KR`         |  | **Kurdish**               | *`string`* | `ku-KU`         |  | **Kyrgyz**                | *`string`* | `ky-KY`         |  | **Lao**                   | *`string`* | `lo-LO`         |  | **Latin**                 | *`string`* | `la-LA`         |  | **Latvian**               | *`string`* | `lv-LV`         |  | **Lithuanian**            | *`string`* | `lt-LT`         |  | **Luxembourgish**         | *`string`* | `lb-LB`         |  | **Macedonian**            | *`string`* | `mk-MK`         |  | **Malagasy**              | *`string`* | `mg-MG`         |  | **Malay**                 | *`string`* | `ms-MY`         |  | **Malayalam**             | *`string`* | `ml-ML`         |  | **Maltese**               | *`string`* | `mt-MT`         |  | **Maori**                 | *`string`* | `mi-MI`         |  | **Marathi**               | *`string`* | `mr-MR`         |  | **Mongolian**             | *`string`* | `mn-MN`         |  | **Myanmar-Burmese**       | *`string`* | `my-MY`         |  | **Nepali**                | *`string`* | `ne-NE`         |  | **Norwegian**             | *`string`* | `no-NO`         |  | **Nyanja Chichewa**       | *`string`* | `ny-NY`         |  | **Pashto**                | *`string`* | `ps-PS`         |  | **Persian**               | *`string`* | `fa-FA`         |  | **Polish**                | *`string`* | `pl-PO`         |  | **Portuguese**            | *`string`* | `pt-PT`         |  | **Punjabi**               | *`string`* | `pa-PA`         |  | **Romanian**              | *`string`* | `ro-RO`         |  | **Russian**               | *`string`* | `ru-RU`         |  | **Samoan**                | *`string`* | `sm-SM`         |  | **Scots Gaelic**          | *`string`* | `gd-GD`         |  | **Serbian**               | *`string`* | `sr-SR`         |  | **Sesotho**               | *`string`* | `st-ST`         |  | **Shona**                 | *`string`* | `sn-SN`         |  | **Sindhi**                | *`string`* | `sd-SD`         |  | **Sinhala-Sinhalese**     | *`string`* | `si-SI`         |  | **Slovak**                | *`string`* | `sk-SK`         |  | **Slovenian**             | *`string`* | `sl-SL`         |  | **Somali**                | *`string`* | `so-SO`         |  | **Spanish**               | *`string`* | `es-ES`         |  | **Sundanese**             | *`string`* | `su-SU`         |  | **Swahili**               | *`string`* | `sh-SH`         |  | **Swedish**               | *`string`* | `sw-SW`         |  | **Tagalog-Filipino**      | *`string`* | `tl-TL`         |  | **Tajik**                 | *`string`* | `tg-TG`         |  | **Tamil**                 | *`string`* | `ta-TA`         |  | **Telugu**                | *`string`* | `te-TE`         |  | **Thai**                  | *`string`* | `th-TH`         |  | **Turkish**               | *`string`* | `tr-TR`         |  | **Ukrainian**             | *`string`* | `uk-UK`         |  | **Urdu**                  | *`string`* | `ur-UR`         |  | **Uzbek**                 | *`string`* | `uz-UZ`         |  | **Vietnamese**            | *`string`* | `vi-VI`         |  | **Welsh**                 | *`string`* | `cy-CY`         |  | **Xhosa**                 | *`string`* | `xh-XH`         |  | **Yiddish**               | *`string`* | `yi-YI`         |  | **Yoruba**                | *`string`* | `yo-YO`         |    **AVAILABLE PROVIDERS**  |Name|Value| |-------------------------------|---------------| | [**IBM Watson**](https://www.edenai.co/catalog/watson-language-translator)|`ibm`|                         |[**Google Cloud Services**](https://www.edenai.co/catalog/google-cloud-translation)|`google`|                         |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-translate)|`amazon`|                         |[**Micrososft Azure**](https://www.edenai.co/catalog/azure-translator)|`microsoft`|    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_translation_with_http_info(text, source_language, target_language, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text: (required)
        :param str source_language: (required)
        :param str target_language: (required)
        :param str providers: (required)
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text', 'source_language', 'target_language', 'providers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method automatic_translation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params or
                params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `automatic_translation`")  # noqa: E501
        # verify the required parameter 'source_language' is set
        if ('source_language' not in params or
                params['source_language'] is None):
            raise ValueError("Missing the required parameter `source_language` when calling `automatic_translation`")  # noqa: E501
        # verify the required parameter 'target_language' is set
        if ('target_language' not in params or
                params['target_language'] is None):
            raise ValueError("Missing the required parameter `target_language` when calling `automatic_translation`")  # noqa: E501
        # verify the required parameter 'providers' is set
        if ('providers' not in params or
                params['providers'] is None):
            raise ValueError("Missing the required parameter `providers` when calling `automatic_translation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'text' in params:
            form_params.append(('text', params['text']))  # noqa: E501
        if 'source_language' in params:
            form_params.append(('source_language', params['source_language']))  # noqa: E501
        if 'target_language' in params:
            form_params.append(('target_language', params['target_language']))  # noqa: E501
        if 'providers' in params:
            form_params.append(('providers', params['providers']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/pretrained/translation/automatic_translation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def langiage_detection(self, text, providers, **kwargs):  # noqa: E501
        """langiage_detection  # noqa: E501

        Language Detection or language guessing is the algorithm of determining which natural language given content is in.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |---------------------------|-------------------------------|---------------| | **English (US)**|*`string`*|`en-US`| | **French**|*`string`*|`fr-FR`| | **Spanish**|*`string`*|`es-ES`|    **AVAILABLE PROVIDERS**  |Name|Value| |-------------------------------|---------------| | [**IBM Watson**](https://www.edenai.co/catalog/watson-language-translator)|`ibm`|                                     |[**Google Cloud Services**](https://www.edenai.co/catalog/google-cloud-translation)|`google`|                                     |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-translate)|`amazon`|                                     |[**Lettria**](https://www.edenai.co/catalog/Lettria)|`lettria`|                                            |[**Micrososft Azure**](https://www.edenai.co/catalog/azure-translator)|`microsoft`|    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.langiage_detection(text, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text: (required)
        :param str providers: (required)
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.langiage_detection_with_http_info(text, providers, **kwargs)  # noqa: E501
        else:
            (data) = self.langiage_detection_with_http_info(text, providers, **kwargs)  # noqa: E501
            return data

    def langiage_detection_with_http_info(self, text, providers, **kwargs):  # noqa: E501
        """langiage_detection  # noqa: E501

        Language Detection or language guessing is the algorithm of determining which natural language given content is in.  **SUPPORTED LANGUAGE**  |Name|Type|Value| |---------------------------|-------------------------------|---------------| | **English (US)**|*`string`*|`en-US`| | **French**|*`string`*|`fr-FR`| | **Spanish**|*`string`*|`es-ES`|    **AVAILABLE PROVIDERS**  |Name|Value| |-------------------------------|---------------| | [**IBM Watson**](https://www.edenai.co/catalog/watson-language-translator)|`ibm`|                                     |[**Google Cloud Services**](https://www.edenai.co/catalog/google-cloud-translation)|`google`|                                     |[**Amazon Web Services**](https://www.edenai.co/catalog/amazon-translate)|`amazon`|                                     |[**Lettria**](https://www.edenai.co/catalog/Lettria)|`lettria`|                                            |[**Micrososft Azure**](https://www.edenai.co/catalog/azure-translator)|`microsoft`|    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.langiage_detection_with_http_info(text, providers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text: (required)
        :param str providers: (required)
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text', 'providers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method langiage_detection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params or
                params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `langiage_detection`")  # noqa: E501
        # verify the required parameter 'providers' is set
        if ('providers' not in params or
                params['providers'] is None):
            raise ValueError("Missing the required parameter `providers` when calling `langiage_detection`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'text' in params:
            form_params.append(('text', params['text']))  # noqa: E501
        if 'providers' in params:
            form_params.append(('providers', params['providers']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/pretrained/translation/language_detection', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
