url = 'https://www.msc.com/track-a-shipment?agencyPath=ind'
formdata = {'__EVENTTARGET':'ctl00$ctl00$plcMain$plcMain$TrackSearch$hlkSearch',
            '__EVENTARGUMENT':'',
            '__LASTFOCUS':'',
            'lng':'en-GB',
            '__VIEWSTATEGENERATOR':'184F8A35',
            'ctl00$ctl00$Header$LanguageSelectionDropDown$ddlSelectLanguage':'en-GB',
            'ctl00$ctl00$Header$HeaderMenuLower$ucHeaderSearchDropdown$txtSearch':'',
            'ctl00$ctl00$Header$HeaderMenuLower$ucHeaderSearchDropdown$vceSearch_ClientState':'',
            'ctl00$ctl00$plcMain$plcMain$TrackSearch$fldTrackingType$DropDownField':'containerbilloflading',
            'ctl00$ctl00$plcMain$plcMain$TrackSearch$txtBolSearch$TextField':'',
            'ctl00$ctl00$plcMain$plcMain$hdnEmailAlertsId':'',
            'ctl00$ctl00$plcMain$plcMain$txtEmail$TextField':'',
            'ctl00$ctl00$plcMain$plcMain$hdnDetailsTrackingType':'',
            'ctl00$ctl00$plcMain$plcMain$hdnDetailsTrackingKey':'',
            'ctl00$ctl00$plcMain$plcMain$TrackingSendForm$fldRecipientName$TextField':'',
            'ctl00$ctl00$plcMain$plcMain$TrackingSendForm$fldRecipientEmail$TextField':'',
            'ctl00$ctl00$plcMain$plcMain$TrackingSendForm$fldSenderName$TextField':'',
            'ctl00$ctl00$plcMain$plcMain$TrackingSendForm$fldSenderEmail$TextField':'',
            'ctl00$ctl00$ucTradeFinanceSignUpModal$hdnFinanceCompanyTerms':'',
            'ctl00$ctl00$ucTradeFinanceSignUpModal$txtName$TextField':'',
            'ctl00$ctl00$ucTradeFinanceSignUpModal$txtEmailAddress$TextField':'',
            'ctl00$ctl00$ucTradeFinanceSignUpModal$txtCompanyName$TextField':'',
            'ctl00$ctl00$ucTradeFinanceSignUpModal$txtPhoneNumber$TextField':'',
            'g-recaptcha-response':'',
            '__VIEWSTATE':'',
            '__EVENTVALIDATION':'',
            }

h3id = '//*[@id="ctl00_ctl00_plcMain_plcMain_pnlTrackingResults"]/h3/text()'
container_info = '//*[@id="ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_rptContainers_ctl01_pnlContainer"]/table[1]/tbody'
container_path = '//*[@id="ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_rptContainers_ctl01_pnlContainer"]/table[2]/tbody/tr'

bol_info =       '//*[@id="ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_pnlBOLContent"]/table/tbody'
bol_num_cont   = '//*[@id="ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_hlkBOLToggle"]/text()'
bol_cont_hdr_ptrn = '//*[@id="ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_rptContainers_ctl%02d_pnlContainer"]/table[1]/tbody'
bol_cont_mov_ptrn = '//*[@id="ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_rptContainers_ctl%02d_pnlContainer"]/table[2]/tbody/tr'
bol_con_name_ptrn = '//*[@id="ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_rptContainers_ctl%02d_hlkContainerToggle"]/text()'

                 
                 

