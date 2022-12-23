<html itemscope="" itemtype="https://schema.org/QAPage" class="html__responsive " lang="en">
    <head>

        <title>c++ - Difference between shared objects (.so), static libraries (.a), and DLL's (.so)? - Stack Overflow</title>
        <link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
        <link rel="apple-touch-icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
        <link rel="image_src" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a"> 
        <link rel="search" type="application/opensearchdescription+xml" title="Stack Overflow" href="/opensearch.xml">
        <link rel="canonical" href="https://stackoverflow.com/questions/9688200/difference-between-shared-objects-so-static-libraries-a-and-dlls-so">
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
        <meta property="og:type" content="website">
        <meta property="og:url" content="https://stackoverflow.com/questions/9688200/difference-between-shared-objects-so-static-libraries-a-and-dlls-so">
        <meta property="og:site_name" content="Stack Overflow">
        <meta property="og:image" itemprop="image primaryImageOfPage" content="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded">
        <meta name="twitter:card" content="summary">
        <meta name="twitter:domain" content="stackoverflow.com">
        <meta name="twitter:title" property="og:title" itemprop="name" content="Difference between shared objects (.so), static libraries (.a), and DLL's (.so)?">
        <meta name="twitter:description" property="og:description" itemprop="description" content="I have been involved in some debate with respect to libraries in Linux, and would like to confirm some things.
It is to my understanding (please correct me if I am wrong and I will edit my post lat...">
    <script id="webpack-public-path" type="text/uri-list">https://cdn.sstatic.net/</script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script defer="" src="https://cdn.sstatic.net/Js/third-party/npm/@stackoverflow/stacks/dist/js/stacks.min.js?v=9bc856be1b3a"></script>
    <script src="https://cdn.sstatic.net/Js/stub.en.js?v=3442317c40c6"></script>


    <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/stacks.css?v=70e4dd648d48">
    <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Sites/stackoverflow/primary.css?v=c05ce93d5306">


    
            <link rel="alternate" type="application/atom+xml" title="Feed for question 'Difference between shared objects (.so), static libraries (.a), and DLL's (.so)?'" href="/feeds/question/9688200">
            <meta name="twitter:app:country" content="US">
            <meta name="twitter:app:name:iphone" content="Stack Exchange iOS">
            <meta name="twitter:app:id:iphone" content="871299723">
            <meta name="twitter:app:url:iphone" content="se-zaphod://stackoverflow.com/questions/9688200/difference-between-shared-objects-so-static-libraries-a-and-dlls-so">
            <meta name="twitter:app:name:ipad" content="Stack Exchange iOS">
            <meta name="twitter:app:id:ipad" content="871299723">
            <meta name="twitter:app:url:ipad" content="se-zaphod://stackoverflow.com/questions/9688200/difference-between-shared-objects-so-static-libraries-a-and-dlls-so">
            <meta name="twitter:app:name:googleplay" content="Stack Exchange Android">
            <meta name="twitter:app:url:googleplay" content="https://stackoverflow.com/questions/9688200/difference-between-shared-objects-so-static-libraries-a-and-dlls-so">
            <meta name="twitter:app:id:googleplay" content="com.stackexchange.marvin">
        <script>
            StackExchange.ready(function () {

                    StackExchange.using("snippets", function () {
                        StackExchange.snippets.initSnippetRenderer();
                    });
                    
                StackExchange.using("postValidation", function () {
                    StackExchange.postValidation.initOnBlurAndSubmit($('#post-form'), 2, 'answer');
                });


                StackExchange.question.init({showAnswerHelp:true,showTrendingSortLaunchPopover:false,showTrendingSortPostLaunchPopover:false,totalCommentCount:8,shownCommentCount:5,enableTables:true,questionId:9688200});

                styleCode();

                    StackExchange.realtime.subscribeToQuestion('1', '9688200');
                    StackExchange.using("gps", function () { StackExchange.gps.trackOutboundClicks('#content', '.js-post-body'); });


            });
        </script>

        
        
        
        <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/Channels/channels.css?v=a5fae8812988">

        
        


    <script type="application/json" data-role="module-args" data-module-name="Shared/options.mod">{"options":{"locale":"en","serverTime":1671808623,"routeName":"Questions/Show","stackAuthUrl":"https://stackauth.com","networkMetaHostname":"meta.stackexchange.com","site":{"name":"Stack Overflow","description":"Q\u0026A for professional and enthusiast programmers","isNoticesTabEnabled":true,"enableNewTagCreationWarning":true,"insertSpaceAfterNameTabCompletion":false,"id":1,"cookieDomain":".stackoverflow.com","childUrl":"https://meta.stackoverflow.com","negativeVoteScoreFloor":null,"enableSocialMediaInSharePopup":true,"protocol":"https"},"user":{"fkey":"57626a78caee3eb0bd6fd5e0940aee94740c698e816bbd2d12d050fc41b3a36d","tid":"4e958f59-97ef-9d7d-e8fc-576ff1451a58","rep":0,"isAnonymous":true,"isAnonymousNetworkWide":true},"events":{"postType":{"question":1},"postEditionSection":{"title":1,"body":2,"tags":3}},"svgIconPath":"https://cdn.sstatic.net/Img/stacks-icons","svgIconHash":"25f5bf79286d"}}</script>
<script type="application/json" data-role="module-args" data-module-name="Shared/settings.mod">{"settings":{"userMessaging":{"showNewFeatureNotice":true},"tags":{},"subscriptions":{"defaultBasicMaxTrueUpSeats":250,"defaultFreemiumMaxTrueUpSeats":50,"defaultMaxTrueUpSeats":1000},"snippets":{"renderDomain":"stacksnippets.net","snippetsEnabled":true},"site":{"allowImageUploads":true,"enableImgurHttps":true,"enableUserHovercards":true,"forceHttpsImages":true,"stacksEditorPreviewEnabled":true,"styleCode":true},"questions":{"enableQuestionTitleLengthLiveWarning":true,"enableSavesFeature":true,"maxTitleSize":150,"questionTitleLengthStartLiveWarningChars":50},"intercom":{"appId":"inf0secd","hostBaseUrl":"https://stacksnippets.net"},"paths":{"jQueryUICSSPath":"https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/themes/smoothness/jquery-ui.css","jQueryUIJSPath":"https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/jquery-ui.min.js"},"monitoring":{"clientTimingsAbsoluteTimeout":30000,"clientTimingsDebounceTimeout":1000},"mentions":{"maxNumUsersInDropdown":50},"markdown":{"enableTables":true},"legal":{"oneTrustConfigId":"c3d9f1e3-55f3-4eba-b268-46cee4c6789c"},"flags":{"allowRetractingCommentFlags":true,"allowRetractingFlags":true},"elections":{"opaVoteResultsBaseUrl":"https://www.opavote.com/results/"},"comments":{},"accounts":{"currentPasswordRequiredForChangingStackIdPassword":true}}}</script>
<script>StackExchange.init();</script>

    <script>
        StackExchange.using.setCacheBreakers({"Js/adops.en.js":"6da43f5e0a84","Js/ask.en.js":"","Js/begin-edit-event.en.js":"dd955babf04d","Js/copy-transpiled.en.js":"e7855bee94f2","Js/events.en.js":"","Js/explore-qlist.en.js":"2b1f34938b8b","Js/full-anon.en.js":"1dd7c4bcf6fa","Js/full.en.js":"7c151a73f46a","Js/highlightjs-loader.en.js":"a284064706b3","Js/inline-tag-editing.en.js":"629d801833ec","Js/keyboard-shortcuts.en.js":"a715495ee04f","Js/markdown-it-loader.en.js":"5818ef89ff9d","Js/moderator.en.js":"626c2dad029e","Js/postCollections-transpiled.en.js":"529276cfb7ae","Js/post-validation.en.js":"cedd65876389","Js/question-editor.en.js":"","Js/review-v2-transpiled.en.js":"9314448c023b","Js/revisions.en.js":"a86490719687","Js/stacks-editor.en.js":"198834eebc62","Js/tageditor.en.js":"825c9597ce2d","Js/tageditornew.en.js":"4340d4f2a34c","Js/tagsuggestions.en.js":"1bcff7d98f97","Js/unlimited-transpiled.en.js":"7ed67670b600","Js/wmd.en.js":"5b83d3f656eb","Js/snippet-javascript-codemirror.en.js":"73fce5cc7219"});
        StackExchange.using("gps", function() {
             StackExchange.gps.init(false);
        });
    </script>
    <noscript id="noscript-css"><style>body,.s-topbar{margin-top:1.9em}</style></noscript>
    <meta http-equiv="origin-trial" content="Az6AfRvI8mo7yiW5fLfj04W21t0ig6aMsGYpIqMTaX60H+b0DkO1uDr+7BrzMcimWzv/X7SXR8jI+uvbV0IJlwYAAACFeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A+USTya+tNvDPaxUgJooz+LaVk5hPoAxpLvSxjogX4Mk8awCTQ9iop6zJ9d5ldgU7WmHqBlnQB41LHHRFxoaBwoAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7FovoGr67TUBYbnY+Z0IKoJbbmRmB8fCyirUGHavNDtD91CiGyHHSA2hDG9r9T3NjUKFi6egL3RbgTwhhcVDwUAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><script src="https://pagead2.googlesyndication.com/gpt/pubads_impl_2022120501.js" async=""></script><script async="" src="https://cdn.sstatic.net/Js/full-anon.en.js?v=1dd7c4bcf6fa"></script><script async="" src="https://cdn.sstatic.net/Js/post-validation.en.js?v=cedd65876389"></script><script src="https://cdn.cookielaw.org/scripttemplates/6.37.0/otBannerSdk.js" async="" type="text/javascript"></script><div id="onetrust-style" class="d-none">#onetrust-banner-sdk{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}#onetrust-banner-sdk .onetrust-vendors-list-handler{cursor:pointer;color:#1f96db;font-size:inherit;font-weight:bold;text-decoration:none;margin-left:5px}#onetrust-banner-sdk .onetrust-vendors-list-handler:hover{color:#1f96db}#onetrust-banner-sdk:focus{outline:2px solid #000;outline-offset:-2px}#onetrust-banner-sdk a:focus{outline:2px solid #000}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{outline-offset:1px}#onetrust-banner-sdk.ot-bnr-w-logo .ot-bnr-logo{height:64px;width:64px}#onetrust-banner-sdk .ot-close-icon,#onetrust-pc-sdk .ot-close-icon,#ot-sync-ntfy .ot-close-icon{background-image:url("data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMzQ4LjMzM3B4IiBoZWlnaHQ9IjM0OC4zMzNweCIgdmlld0JveD0iMCAwIDM0OC4zMzMgMzQ4LjMzNCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMzQ4LjMzMyAzNDguMzM0OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+PGc+PHBhdGggZmlsbD0iIzU2NTY1NiIgZD0iTTMzNi41NTksNjguNjExTDIzMS4wMTYsMTc0LjE2NWwxMDUuNTQzLDEwNS41NDljMTUuNjk5LDE1LjcwNSwxNS42OTksNDEuMTQ1LDAsNTYuODVjLTcuODQ0LDcuODQ0LTE4LjEyOCwxMS43NjktMjguNDA3LDExLjc2OWMtMTAuMjk2LDAtMjAuNTgxLTMuOTE5LTI4LjQxOS0xMS43NjlMMTc0LjE2NywyMzEuMDAzTDY4LjYwOSwzMzYuNTYzYy03Ljg0Myw3Ljg0NC0xOC4xMjgsMTEuNzY5LTI4LjQxNiwxMS43NjljLTEwLjI4NSwwLTIwLjU2My0zLjkxOS0yOC40MTMtMTEuNzY5Yy0xNS42OTktMTUuNjk4LTE1LjY5OS00MS4xMzksMC01Ni44NWwxMDUuNTQtMTA1LjU0OUwxMS43NzQsNjguNjExYy0xNS42OTktMTUuNjk5LTE1LjY5OS00MS4xNDUsMC01Ni44NDRjMTUuNjk2LTE1LjY4Nyw0MS4xMjctMTUuNjg3LDU2LjgyOSwwbDEwNS41NjMsMTA1LjU1NEwyNzkuNzIxLDExLjc2N2MxNS43MDUtMTUuNjg3LDQxLjEzOS0xNS42ODcsNTYuODMyLDBDMzUyLjI1OCwyNy40NjYsMzUyLjI1OCw1Mi45MTIsMzM2LjU1OSw2OC42MTF6Ii8+PC9nPjwvc3ZnPg==");background-size:contain;background-repeat:no-repeat;background-position:center;height:12px;width:12px}#onetrust-banner-sdk .powered-by-logo,#onetrust-banner-sdk .ot-pc-footer-logo a,#onetrust-pc-sdk .powered-by-logo,#onetrust-pc-sdk .ot-pc-footer-logo a,#ot-sync-ntfy .powered-by-logo,#ot-sync-ntfy .ot-pc-footer-logo a{background-size:contain;background-repeat:no-repeat;background-position:center;height:25px;width:152px;display:block;text-decoration:none;font-size:0.75em}#onetrust-banner-sdk .powered-by-logo:hover,#onetrust-banner-sdk .ot-pc-footer-logo a:hover,#onetrust-pc-sdk .powered-by-logo:hover,#onetrust-pc-sdk .ot-pc-footer-logo a:hover,#ot-sync-ntfy .powered-by-logo:hover,#ot-sync-ntfy .ot-pc-footer-logo a:hover{color:#565656}#onetrust-banner-sdk h3 *,#onetrust-banner-sdk h4 *,#onetrust-banner-sdk h6 *,#onetrust-banner-sdk button *,#onetrust-banner-sdk a[data-parent-id] *,#onetrust-pc-sdk h3 *,#onetrust-pc-sdk h4 *,#onetrust-pc-sdk h6 *,#onetrust-pc-sdk button *,#onetrust-pc-sdk a[data-parent-id] *,#ot-sync-ntfy h3 *,#ot-sync-ntfy h4 *,#ot-sync-ntfy h6 *,#ot-sync-ntfy button *,#ot-sync-ntfy a[data-parent-id] *{font-size:inherit;font-weight:inherit;color:inherit}#onetrust-banner-sdk .ot-hide,#onetrust-pc-sdk .ot-hide,#ot-sync-ntfy .ot-hide{display:none !important}#onetrust-banner-sdk button.ot-link-btn:hover,#onetrust-pc-sdk button.ot-link-btn:hover,#ot-sync-ntfy button.ot-link-btn:hover{text-decoration:underline;opacity:1}#onetrust-pc-sdk .ot-sdk-row .ot-sdk-column{padding:0}#onetrust-pc-sdk .ot-sdk-container{padding-right:0}#onetrust-pc-sdk .ot-sdk-row{flex-direction:initial;width:100%}#onetrust-pc-sdk [type="checkbox"]:checked,#onetrust-pc-sdk [type="checkbox"]:not(:checked){pointer-events:initial}#onetrust-pc-sdk [type="checkbox"]:disabled+label::before,#onetrust-pc-sdk [type="checkbox"]:disabled+label:after,#onetrust-pc-sdk [type="checkbox"]:disabled+label{pointer-events:none;opacity:0.7}#onetrust-pc-sdk #vendor-list-content{transform:translate3d(0, 0, 0)}#onetrust-pc-sdk li input[type="checkbox"]{z-index:1}#onetrust-pc-sdk li .ot-checkbox label{z-index:2}#onetrust-pc-sdk li .ot-checkbox input[type="checkbox"]{height:auto;width:auto}#onetrust-pc-sdk li .host-title a,#onetrust-pc-sdk li .ot-host-name a,#onetrust-pc-sdk li .accordion-text,#onetrust-pc-sdk li .ot-acc-txt{z-index:2;position:relative}#onetrust-pc-sdk input{margin:3px 0.1ex}#onetrust-pc-sdk .pc-logo,#onetrust-pc-sdk .ot-pc-logo{height:60px;width:180px;background-position:center;background-size:contain;background-repeat:no-repeat}#onetrust-pc-sdk .screen-reader-only,#onetrust-pc-sdk .ot-scrn-rdr,.ot-sdk-cookie-policy .screen-reader-only,.ot-sdk-cookie-policy .ot-scrn-rdr{border:0;clip:rect(0 0 0 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}#onetrust-pc-sdk.ot-fade-in,.onetrust-pc-dark-filter.ot-fade-in,#onetrust-banner-sdk.ot-fade-in{animation-name:onetrust-fade-in;animation-duration:400ms;animation-timing-function:ease-in-out}#onetrust-pc-sdk.ot-hide{display:none !important}.onetrust-pc-dark-filter.ot-hide{display:none !important}#ot-sdk-btn.ot-sdk-show-settings,#ot-sdk-btn.optanon-show-settings{color:#68b631;border:1px solid #68b631;height:auto;white-space:normal;word-wrap:break-word;padding:0.8em 2em;font-size:0.8em;line-height:1.2;cursor:pointer;-moz-transition:0.1s ease;-o-transition:0.1s ease;-webkit-transition:1s ease;transition:0.1s ease}#ot-sdk-btn.ot-sdk-show-settings:hover,#ot-sdk-btn.optanon-show-settings:hover{color:#fff;background-color:#68b631}.onetrust-pc-dark-filter{background:rgba(0,0,0,0.5);z-index:2147483646;width:100%;height:100%;overflow:hidden;position:fixed;top:0;bottom:0;left:0}@keyframes onetrust-fade-in{0%{opacity:0}100%{opacity:1}}.ot-cookie-label{text-decoration:underline}@media only screen and (min-width: 426px) and (max-width: 896px) and (orientation: landscape){#onetrust-pc-sdk p{font-size:0.75em}}#onetrust-banner-sdk .banner-option-input:focus+label{outline:1px solid #000;outline-style:auto}.category-vendors-list-handler+a:focus,.category-vendors-list-handler+a:focus-visible{outline:2px solid #000}#onetrust-pc-sdk .ot-userid-title{margin-top:10px}#onetrust-pc-sdk .ot-userid-title&gt;span,#onetrust-pc-sdk .ot-userid-timestamp&gt;span{font-weight:700}#onetrust-pc-sdk .ot-userid-desc{font-style:italic}#onetrust-pc-sdk .ot-host-desc a{pointer-events:initial}#onetrust-pc-sdk .ot-ven-hdr&gt;p a{position:relative;z-index:2;pointer-events:initial}#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info a,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info a{margin-right:auto}
#onetrust-banner-sdk,#onetrust-pc-sdk,#ot-sdk-cookie-policy,#ot-sync-ntfy{font-size:16px}#onetrust-banner-sdk *,#onetrust-banner-sdk ::after,#onetrust-banner-sdk ::before,#onetrust-pc-sdk *,#onetrust-pc-sdk ::after,#onetrust-pc-sdk ::before,#ot-sdk-cookie-policy *,#ot-sdk-cookie-policy ::after,#ot-sdk-cookie-policy ::before,#ot-sync-ntfy *,#ot-sync-ntfy ::after,#ot-sync-ntfy ::before{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}#onetrust-banner-sdk div,#onetrust-banner-sdk span,#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-banner-sdk p,#onetrust-banner-sdk img,#onetrust-banner-sdk svg,#onetrust-banner-sdk button,#onetrust-banner-sdk section,#onetrust-banner-sdk a,#onetrust-banner-sdk label,#onetrust-banner-sdk input,#onetrust-banner-sdk ul,#onetrust-banner-sdk li,#onetrust-banner-sdk nav,#onetrust-banner-sdk table,#onetrust-banner-sdk thead,#onetrust-banner-sdk tr,#onetrust-banner-sdk td,#onetrust-banner-sdk tbody,#onetrust-banner-sdk .ot-main-content,#onetrust-banner-sdk .ot-toggle,#onetrust-banner-sdk #ot-content,#onetrust-banner-sdk #ot-pc-content,#onetrust-banner-sdk .checkbox,#onetrust-pc-sdk div,#onetrust-pc-sdk span,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#onetrust-pc-sdk p,#onetrust-pc-sdk img,#onetrust-pc-sdk svg,#onetrust-pc-sdk button,#onetrust-pc-sdk section,#onetrust-pc-sdk a,#onetrust-pc-sdk label,#onetrust-pc-sdk input,#onetrust-pc-sdk ul,#onetrust-pc-sdk li,#onetrust-pc-sdk nav,#onetrust-pc-sdk table,#onetrust-pc-sdk thead,#onetrust-pc-sdk tr,#onetrust-pc-sdk td,#onetrust-pc-sdk tbody,#onetrust-pc-sdk .ot-main-content,#onetrust-pc-sdk .ot-toggle,#onetrust-pc-sdk #ot-content,#onetrust-pc-sdk #ot-pc-content,#onetrust-pc-sdk .checkbox,#ot-sdk-cookie-policy div,#ot-sdk-cookie-policy span,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy p,#ot-sdk-cookie-policy img,#ot-sdk-cookie-policy svg,#ot-sdk-cookie-policy button,#ot-sdk-cookie-policy section,#ot-sdk-cookie-policy a,#ot-sdk-cookie-policy label,#ot-sdk-cookie-policy input,#ot-sdk-cookie-policy ul,#ot-sdk-cookie-policy li,#ot-sdk-cookie-policy nav,#ot-sdk-cookie-policy table,#ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy tr,#ot-sdk-cookie-policy td,#ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy .ot-main-content,#ot-sdk-cookie-policy .ot-toggle,#ot-sdk-cookie-policy #ot-content,#ot-sdk-cookie-policy #ot-pc-content,#ot-sdk-cookie-policy .checkbox,#ot-sync-ntfy div,#ot-sync-ntfy span,#ot-sync-ntfy h1,#ot-sync-ntfy h2,#ot-sync-ntfy h3,#ot-sync-ntfy h4,#ot-sync-ntfy h5,#ot-sync-ntfy h6,#ot-sync-ntfy p,#ot-sync-ntfy img,#ot-sync-ntfy svg,#ot-sync-ntfy button,#ot-sync-ntfy section,#ot-sync-ntfy a,#ot-sync-ntfy label,#ot-sync-ntfy input,#ot-sync-ntfy ul,#ot-sync-ntfy li,#ot-sync-ntfy nav,#ot-sync-ntfy table,#ot-sync-ntfy thead,#ot-sync-ntfy tr,#ot-sync-ntfy td,#ot-sync-ntfy tbody,#ot-sync-ntfy .ot-main-content,#ot-sync-ntfy .ot-toggle,#ot-sync-ntfy #ot-content,#ot-sync-ntfy #ot-pc-content,#ot-sync-ntfy .checkbox{font-family:inherit;font-weight:normal;-webkit-font-smoothing:auto;letter-spacing:normal;line-height:normal;padding:0;margin:0;height:auto;min-height:0;max-height:none;width:auto;min-width:0;max-width:none;border-radius:0;border:none;clear:none;float:none;position:static;bottom:auto;left:auto;right:auto;top:auto;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;white-space:normal;background:none;overflow:visible;vertical-align:baseline;visibility:visible;z-index:auto;box-shadow:none}#onetrust-banner-sdk label:before,#onetrust-banner-sdk label:after,#onetrust-banner-sdk .checkbox:after,#onetrust-banner-sdk .checkbox:before,#onetrust-pc-sdk label:before,#onetrust-pc-sdk label:after,#onetrust-pc-sdk .checkbox:after,#onetrust-pc-sdk .checkbox:before,#ot-sdk-cookie-policy label:before,#ot-sdk-cookie-policy label:after,#ot-sdk-cookie-policy .checkbox:after,#ot-sdk-cookie-policy .checkbox:before,#ot-sync-ntfy label:before,#ot-sync-ntfy label:after,#ot-sync-ntfy .checkbox:after,#ot-sync-ntfy .checkbox:before{content:"";content:none}
#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{position:relative;width:100%;max-width:100%;margin:0 auto;padding:0 20px;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{width:100%;float:left;box-sizing:border-box;padding:0;display:initial}@media (min-width: 400px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:90%;padding:0}}@media (min-width: 550px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:100%}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{margin-left:4%}#onetrust-banner-sdk .ot-sdk-column:first-child,#onetrust-banner-sdk .ot-sdk-columns:first-child,#onetrust-pc-sdk .ot-sdk-column:first-child,#onetrust-pc-sdk .ot-sdk-columns:first-child,#ot-sdk-cookie-policy .ot-sdk-column:first-child,#ot-sdk-cookie-policy .ot-sdk-columns:first-child{margin-left:0}#onetrust-banner-sdk .ot-sdk-two.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-two.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-two.ot-sdk-columns{width:13.3333333333%}#onetrust-banner-sdk .ot-sdk-three.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-three.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-three.ot-sdk-columns{width:22%}#onetrust-banner-sdk .ot-sdk-four.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-four.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-four.ot-sdk-columns{width:30.6666666667%}#onetrust-banner-sdk .ot-sdk-eight.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eight.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eight.ot-sdk-columns{width:65.3333333333%}#onetrust-banner-sdk .ot-sdk-nine.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-nine.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-nine.ot-sdk-columns{width:74%}#onetrust-banner-sdk .ot-sdk-ten.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-ten.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-ten.ot-sdk-columns{width:82.6666666667%}#onetrust-banner-sdk .ot-sdk-eleven.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eleven.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eleven.ot-sdk-columns{width:91.3333333333%}#onetrust-banner-sdk .ot-sdk-twelve.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-twelve.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-twelve.ot-sdk-columns{width:100%;margin-left:0}}#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6{margin-top:0;font-weight:600;font-family:inherit}#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem;line-height:1.2}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem;line-height:1.25}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem;line-height:1.3}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem;line-height:1.35}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem;line-height:1.5}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem;line-height:1.6}@media (min-width: 550px){#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem}}#onetrust-banner-sdk p,#onetrust-pc-sdk p,#ot-sdk-cookie-policy p{margin:0 0 1em 0;font-family:inherit;line-height:normal}#onetrust-banner-sdk a,#onetrust-pc-sdk a,#ot-sdk-cookie-policy a{color:#565656;text-decoration:underline}#onetrust-banner-sdk a:hover,#onetrust-pc-sdk a:hover,#ot-sdk-cookie-policy a:hover{color:#565656;text-decoration:none}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{display:inline-block;height:38px;padding:0 30px;color:#555;text-align:center;font-size:0.9em;font-weight:400;line-height:38px;letter-spacing:0.01em;text-decoration:none;white-space:nowrap;background-color:transparent;border-radius:2px;border:1px solid #bbb;cursor:pointer;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-button:hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):focus,#onetrust-pc-sdk .ot-sdk-button:hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):focus,#ot-sdk-cookie-policy .ot-sdk-button:hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)&gt;button:not(.ot-link-btn):focus{color:#333;border-color:#888;opacity:0.7}#onetrust-banner-sdk .ot-sdk-button:focus,#onetrust-banner-sdk :not(.ot-leg-btn-container)&gt;button:focus,#onetrust-pc-sdk .ot-sdk-button:focus,#onetrust-pc-sdk :not(.ot-leg-btn-container)&gt;button:focus,#ot-sdk-cookie-policy .ot-sdk-button:focus,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)&gt;button:focus{outline:2px solid #000}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-banner-sdk button.ot-sdk-button-primary,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-pc-sdk button.ot-sdk-button-primary,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary,#ot-sdk-cookie-policy button.ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary{color:#fff;background-color:#33c3f0;border-color:#33c3f0}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-banner-sdk button.ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary:hover,#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-banner-sdk button.ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary:focus,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-pc-sdk button.ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary:hover,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-pc-sdk button.ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary:focus{color:#fff;background-color:#1eaedb;border-color:#1eaedb}#onetrust-banner-sdk input[type="text"],#onetrust-pc-sdk input[type="text"],#ot-sdk-cookie-policy input[type="text"]{height:38px;padding:6px 10px;background-color:#fff;border:1px solid #d1d1d1;border-radius:4px;box-shadow:none;box-sizing:border-box}#onetrust-banner-sdk input[type="text"],#onetrust-pc-sdk input[type="text"],#ot-sdk-cookie-policy input[type="text"]{-webkit-appearance:none;-moz-appearance:none;appearance:none}#onetrust-banner-sdk input[type="text"]:focus,#onetrust-pc-sdk input[type="text"]:focus,#ot-sdk-cookie-policy input[type="text"]:focus{border:1px solid #000;outline:0}#onetrust-banner-sdk label,#onetrust-pc-sdk label,#ot-sdk-cookie-policy label{display:block;margin-bottom:0.5rem;font-weight:600}#onetrust-banner-sdk input[type="checkbox"],#onetrust-pc-sdk input[type="checkbox"],#ot-sdk-cookie-policy input[type="checkbox"]{display:inline}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{list-style:circle inside}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{padding-left:0;margin-top:0}#onetrust-banner-sdk ul ul,#onetrust-pc-sdk ul ul,#ot-sdk-cookie-policy ul ul{margin:1.5rem 0 1.5rem 3rem;font-size:90%}#onetrust-banner-sdk li,#onetrust-pc-sdk li,#ot-sdk-cookie-policy li{margin-bottom:1rem}#onetrust-banner-sdk th,#onetrust-banner-sdk td,#onetrust-pc-sdk th,#onetrust-pc-sdk td,#ot-sdk-cookie-policy th,#ot-sdk-cookie-policy td{padding:12px 15px;text-align:left;border-bottom:1px solid #e1e1e1}#onetrust-banner-sdk button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-container:after,#onetrust-banner-sdk .ot-sdk-row:after,#onetrust-pc-sdk .ot-sdk-container:after,#onetrust-pc-sdk .ot-sdk-row:after,#ot-sdk-cookie-policy .ot-sdk-container:after,#ot-sdk-cookie-policy .ot-sdk-row:after{content:"";display:table;clear:both}#onetrust-banner-sdk .ot-sdk-row,#onetrust-pc-sdk .ot-sdk-row,#ot-sdk-cookie-policy .ot-sdk-row{margin:0;max-width:none;display:block}
.ot-sdk-cookie-policy{font-family:inherit;font-size:16px}.ot-sdk-cookie-policy.otRelFont{font-size:1rem}.ot-sdk-cookie-policy h3,.ot-sdk-cookie-policy h4,.ot-sdk-cookie-policy h6,.ot-sdk-cookie-policy p,.ot-sdk-cookie-policy li,.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy th,.ot-sdk-cookie-policy #cookie-policy-description,.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}.ot-sdk-cookie-policy h4{font-size:1.2em}.ot-sdk-cookie-policy h6{font-size:1em;margin-top:2em}.ot-sdk-cookie-policy th{min-width:75px}.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy a:hover{background:#fff}.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}.ot-sdk-cookie-policy .ot-mobile-border{display:none}.ot-sdk-cookie-policy section{margin-bottom:2em}.ot-sdk-cookie-policy table{border-collapse:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy{font-family:inherit;font-size:1rem}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup{margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group-desc,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-table-header,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td{font-size:.9em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td a{font-size:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group{font-size:1em;margin-bottom:.6em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-title{margin-bottom:1.2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy&gt;section{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th{min-width:75px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a:hover{background:#fff}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-mobile-border{display:none}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy section{margin-bottom:2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li{list-style:disc;margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li h4{display:inline-block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{border-collapse:inherit;margin:auto;border:1px solid #d7d7d7;border-radius:5px;border-spacing:initial;width:100%;overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border-bottom:1px solid #d7d7d7;border-right:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr th:last-child,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr td:last-child{border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:25%}.ot-sdk-cookie-policy[dir=rtl]{text-align:left}#ot-sdk-cookie-policy h3{font-size:1.5em}@media only screen and (max-width: 530px){.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) table,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tbody,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) th,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{display:block}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead tr{position:absolute;top:-9999px;left:-9999px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{margin:0 0 1em 0}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd),.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd) a{background:#f6f6f4}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td{border:none;border-bottom:1px solid #eee;position:relative;padding-left:50%}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{position:absolute;height:100%;left:6px;width:40%;padding-right:10px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) .ot-mobile-border{display:inline-block;background-color:#e4e4e4;position:absolute;height:100%;top:0;left:45%;width:2px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{content:attr(data-label);font-weight:bold}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border:none;border-bottom:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{display:block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:auto}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{margin:0 0 1em 0}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{height:100%;width:40%;padding-right:10px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{content:attr(data-label);font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead tr{position:absolute;top:-9999px;left:-9999px;z-index:-9999}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:1px solid #d7d7d7;border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td:last-child{border-bottom:0px}}
                
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h5,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group {
                        color: #696969;
                    }
                    
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title {
                            color: #696969;
                        }
                    
            
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th {
                            background-color: #F8F8F8;
                        }
                    
            .ot-floating-button__front{background-image:url('https://cdn.cookielaw.org/logos/static/ot_persistent_cookie.png')}</div></head><body class="question-page unified-theme">
    <div id="notify-container"></div>
    <div id="custom-header"></div>
        
<header class="s-topbar ps-fixed t0 l0 js-top-bar">
	<div class="s-topbar--container">
			<a href="#" class="s-topbar--menu-btn js-left-sidebar-toggle" role="menuitem" aria-haspopup="true" aria-controls="left-sidebar" aria-expanded="false"><span></span></a>
			<div class="topbar-dialog leftnav-dialog js-leftnav-dialog dno">
				<div class="left-sidebar js-unpinned-left-sidebar" data-can-be="left-sidebar" data-is-here-when="sm"></div>
			</div>
				<a href="https://stackoverflow.com" class="s-topbar--logo js-gps-track" data-gps-track="top_nav.click({is_current:false, location:2, destination:8})">
					<span class="-img _glyph">Stack Overflow</span>
				</a>



			<ol class="s-navigation" role="presentation">

					<li class="md:d-none">
						<a href="https://stackoverflow.co/" class="s-navigation--item js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;about menu click&quot;,null,null,null]">About</a>
					</li>

				<li>
					<a href="#" class="s-navigation--item js-gps-track js-products-menu" aria-controls="products-popover" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="bottom" data-s-popover-toggle-class="is-selected" data-gps-track="top_nav.products.click({location:2, destination:1})" data-ga="[&quot;top navigation&quot;,&quot;products menu click&quot;,null,null,null]" aria-expanded="false">
						Products
					</a>
				</li>

					<li class="md:d-none">
						<a href="/teams" class="s-navigation--item js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;learn more - teams&quot;,null,null,null]">For Teams</a>
					</li>
			</ol>
			<div class="s-popover ws2 mtn2 p0" id="products-popover" role="menu" aria-hidden="true">
				<div class="s-popover--arrow"></div>
				<ol class="list-reset s-anchors s-anchors__inherit">
					<li class="m6">
						<a href="/questions" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:2})" data-ga="[&quot;top navigation&quot;,&quot;public qa submenu click&quot;,null,null,null]">
							<span class="fs-body1 d-block">Stack Overflow</span>
							<span class="fs-caption d-block fc-light">Public questions &amp; answers</span>
						</a>
					</li>
					<li class="m6">
						<a href="/teams" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:3})" data-ga="[&quot;top navigation&quot;,&quot;teams submenu click&quot;,null,null,null]">
							<span class="fs-body1 d-block">Stack Overflow for Teams</span>
							<span class="fs-caption d-block fc-light">Where developers &amp; technologists share private knowledge with coworkers</span>
						</a>
					</li>
					<li class="m6">
						<a href="https://stackoverflow.co/talent" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:5})" data-ga="[&quot;top navigation&quot;,&quot;talent submenu click&quot;,null,null,null]">
							<span class="fs-body1 d-block">Talent</span>
							<span class="fs-caption d-block fc-light">
								Build your employer brand
							</span>
						</a>
					</li>
					<li class="m6">
						<a href="https://stackoverflow.co/advertising" class="bar-sm p6 d-block h:bg-black-100 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:6})" data-ga="[&quot;top navigation&quot;,&quot;advertising submenu click&quot;,null,null,null]">
							<span class="fs-body1 d-block">Advertising</span>
							<span class="fs-caption d-block fc-light">Reach developers &amp; technologists worldwide</span>
						</a>
					</li>
					<li class="bg-black-025 bt bc-black-075 py6 px6 bbr-md">
						<a href="https://stackoverflow.co/" class="fc-light d-block py6 px6 h:fc-black-800 js-gps-track" data-gps-track="top_nav.products.click({location:2, destination:7})" data-ga="[&quot;top navigation&quot;,&quot;about submenu click&quot;,null,null,null]">About the company</a>
					</li>
				</ol>
			</div>


			<form id="search" role="search" action="/search" class="s-topbar--searchbar js-searchbar " autocomplete="off">
					<div class="s-topbar--searchbar--input-group">
						<input name="q" type="text" role="combobox" placeholder="Search…" value="" autocomplete="off" maxlength="240" class="s-input s-input__search js-search-field " aria-label="Search" aria-controls="top-search" data-controller="s-popover" data-action="focus->s-popover#show" data-s-popover-placement="bottom-start" aria-expanded="false">
						<svg aria-hidden="true" class="s-input-icon s-input-icon__search svg-icon iconSearch" width="18" height="18" viewBox="0 0 18 18"><path d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18l1.5-1.5ZM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0Z"></path></svg>
						<div class="s-popover p0 wmx100 wmn4 sm:wmn-initial js-top-search-popover" id="top-search" role="menu">
    <div class="s-popover--arrow"></div>
    <div class="js-spinner p24 d-flex ai-center jc-center d-none">
        <div class="s-spinner s-spinner__sm fc-orange-400">
            <div class="v-visible-sr">Loading…</div>
        </div>
    </div>

    <span class="v-visible-sr js-screen-reader-info"></span>
    <div class="js-ac-results overflow-y-auto hmx3 d-none"></div>

    <div class="js-search-hints" aria-describedby="Tips for searching"></div>
</div>
					</div>
			</form>
		
<nav class="h100 ml-auto overflow-x-auto pr12">
    <ol class="s-topbar--content" role="menubar">
    
    
    
        <li class="js-topbar-dialog-corral" role="presentation">
                

    <div class="topbar-dialog siteSwitcher-dialog dno" role="menu">
        <div class="header fw-wrap">
            <h3 class="flex--item">
                <a href="https://stackoverflow.com">current community</a>
            </h3>
            <div class="flex--item fl1">
                <div class="ai-center d-flex jc-end">
                    <button class="js-close-button s-btn s-btn__muted p0 ml8 d-none sm:d-block" type="button" aria-label="Close">
                        <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9 15 4.41Z"></path></svg>
                    </button>
                </div>
            </div>
        </div>
        <div class="modal-content bg-powder-050 current-site-container">
            <ul class="current-site ">
                    <li class="d-flex">
                            <div class="fl1">
                <a href="https://stackoverflow.com" class="current-site-link site-link js-gps-track d-flex gs8 gsx" data-id="1" data-gps-track="site_switcher.click({ item_type:3 })">
        <div class="favicon favicon-stackoverflow site-icon flex--item" title="Stack Overflow"></div>
        <span class="flex--item fl1">
            Stack Overflow
        </span>
    </a>

    </div>
    <div class="related-links">
            <a href="https://stackoverflow.com/help" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:14 })">help</a>
            <a href="https://chat.stackoverflow.com/?tab=site&amp;host=stackoverflow.com" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:6 })">chat</a>
    </div>

                    </li>
                    <li class="related-site d-flex">
                            <div class="L-shaped-icon-container">
        <span class="L-shaped-icon"></span>
    </div>

                            <a href="https://meta.stackoverflow.com" class=" site-link js-gps-track d-flex gs8 gsx" data-id="552" data-gps-track="site.switch({ target_site:552, item_type:3 }),site_switcher.click({ item_type:4 })">
        <div class="favicon favicon-stackoverflowmeta site-icon flex--item" title="Meta Stack Overflow"></div>
        <span class="flex--item fl1">
            Meta Stack Overflow
        </span>
    </a>

                    </li>
            </ul>
        </div>

        <div class="header" id="your-communities-header">
            <h3>
your communities            </h3>

        </div>
        <div class="modal-content" id="your-communities-section">

                <div class="call-to-login">
<a href="https://stackoverflow.com/users/signup?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f9688200%2fdifference-between-shared-objects-so-static-libraries-a-and-dlls-so" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:10 })">Sign up</a> or <a href="https://stackoverflow.com/users/login?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f9688200%2fdifference-between-shared-objects-so-static-libraries-a-and-dlls-so" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:11 })">log in</a> to customize your list.                </div>
        </div>

        <div class="header">
            <h3><a href="https://stackexchange.com/sites">more stack exchange communities</a>
            </h3>
            <a href="https://stackoverflow.blog" class="float-right">company blog</a>
        </div>
        <div class="modal-content">
                <div class="child-content"></div>
        </div>        
    </div>

        </li>
    
            <li role="none"><button class="s-topbar--item s-btn s-btn__icon s-btn__muted d-none sm:d-inline-flex js-searchbar-trigger" role="menuitem" aria-label="Search" aria-haspopup="true" aria-controls="search" title="Click to show search"><svg aria-hidden="true" class="svg-icon iconSearch" width="18" height="18" viewBox="0 0 18 18"><path d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18l1.5-1.5ZM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0Z"></path></svg></button></li>
                        <li role="none">
                            <a href="https://stackoverflow.com/users/login?ssrc=head&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f9688200%2fdifference-between-shared-objects-so-static-libraries-a-and-dlls-so" class="s-topbar--item s-topbar--item__unset s-btn s-btn__filled ws-nowrap js-gps-track" role="menuitem" rel="nofollow" data-gps-track="login.click" data-ga="[&quot;top navigation&quot;,&quot;login button click&quot;,null,null,null]">Log in</a>
                        </li>
                        <li role="none"><a href="https://stackoverflow.com/users/signup?ssrc=head&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f9688200%2fdifference-between-shared-objects-so-static-libraries-a-and-dlls-so" class="s-topbar--item s-topbar--item__unset ml4 s-btn s-btn__primary ws-nowrap" role="menuitem" rel="nofollow" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;Header&quot;,null,null]">Sign up</a></li>
    </ol>
</nav>


	</div>
</header>

	<script>
		StackExchange.ready(function () { StackExchange.topbar.init(); });
		StackExchange.scrollPadding.setPaddingTop(50, 10); 
	</script>





    <div class="container">
            

<div id="left-sidebar" data-is-here-when="md lg" class="left-sidebar js-pinned-left-sidebar ps-relative">
    <div class="left-sidebar--sticky-container js-sticky-leftnav">
        <nav role="navigation">
            <ol class="nav-links">
                    

<li class="ps-relative" aria-current="false">


    <a href="/" class="pl8 js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current: false, location:2, destination:8})" aria-controls="" data-controller="" data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
            <div class="d-flex ai-center">
                <div class="flex--item truncate">
                    Home
                </div>
            </div>
    </a>
</li>

                <li>
                    <ol class="nav-links">
                            <li class="fs-fine tt-uppercase ml8 mt16 mb4 fc-light">Public</li>

                            

<li class="ps-relative  youarehere" aria-current="true">


    <a id="nav-questions" href="/questions" class="pl8 js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: true, location:2, destination:1})" aria-controls="" data-controller="" data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
<svg aria-hidden="true" class="svg-icon iconGlobe" width="18" height="18" viewBox="0 0 18 18"><path d="M9 1C4.64 1 1 4.64 1 9c0 4.36 3.64 8 8 8 4.36 0 8-3.64 8-8 0-4.36-3.64-8-8-8ZM8 15.32a6.46 6.46 0 0 1-4.3-2.74 6.46 6.46 0 0 1-.93-5.01L7 11.68v.8c0 .88.12 1.32 1 1.32v1.52Zm5.72-2c-.2-.66-1-1.32-1.72-1.32h-1v-2c0-.44-.56-1-1-1H6V7h1c.44 0 1-.56 1-1V5h2c.88 0 1.4-.72 1.4-1.6v-.33a6.45 6.45 0 0 1 3.83 4.51 6.45 6.45 0 0 1-1.51 5.73v.01Z"></path></svg>            <span class="-link--channel-name">Questions</span>
    </a>
</li>

                                

<li class="ps-relative" aria-current="false">


    <a id="nav-tags" href="/tags" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current: false, location:2, destination:2})" aria-controls="" data-controller="" data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
            <div class="d-flex ai-center">
                <div class="flex--item truncate">
                    Tags
                </div>
            </div>
    </a>
</li>

                                

<li class="ps-relative" aria-current="false">


    <a id="nav-users" href="/users" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current: false, location:2, destination:3})" aria-controls="" data-controller="" data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
            <div class="d-flex ai-center">
                <div class="flex--item truncate">
                    Users
                </div>
            </div>
    </a>
</li>

                                    

<li class="ps-relative" aria-current="false">


    <a id="nav-companies" href="https://stackoverflow.com/jobs/companies?so_medium=stackoverflow&amp;so_source=SiteNav" class=" js-gps-track nav-links--link" data-gps-track="top_nav.click({is_current: false, location:2, destination:12})" aria-controls="" data-controller="" data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
            <div class="d-flex ai-center">
                <div class="flex--item truncate">
                    Companies
                </div>
            </div>
    </a>
</li>

                                <li class="d-flex ml8 mt16 jc-space-between">
                                    <div class="flex--item tt-uppercase tt-uppercase fs-fine fc-light">Collectives</div>
                                    <div class="flex--item fs-fine fc-light">
                                        <a href="javascript:void(0)" class="s-link s-link__inherit mr8 js-gps-track js-collectives-navcta-toggle" role="button" aria-controls="popover-discover-collectives" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="top" data-s-popover-toggle-class="is-selected" data-gps-track="top_nav.click({is_current:false, location:2, destination:17})" aria-expanded="false">
                                            <svg aria-hidden="true" class="svg-icon iconInfoSm" width="14" height="14" viewBox="0 0 14 14"><path d="M7 1a6 6 0 1 1 0 12A6 6 0 0 1 7 1Zm1 10V6H6v5h2Zm0-6V3H6v2h2Z"></path></svg>
                                        </a>
                                    </div>
                                </li>
                                    

<li class="ps-relative" aria-current="false">


    <a id="nav-collective-discover" href="/collectives" class="pl8 ai-center js-collectives-navcta-toggle js-gps-track nav-links--link -link__with-icon" data-gps-track="top_nav.click({is_current: false, location:2, destination:18})" aria-controls="" data-controller="" data-s-popover-placement="right" aria-current="false" data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never">
<svg aria-hidden="true" class="mt-auto fc-orange-400 svg-icon iconStarVerified" width="18" height="18" viewBox="0 0 18 18"><path d="M9.86.89a1.14 1.14 0 0 0-1.72 0l-.5.58c-.3.35-.79.48-1.23.33l-.72-.25a1.14 1.14 0 0 0-1.49.85l-.14.76c-.1.45-.45.8-.9.9l-.76.14c-.67.14-1.08.83-.85 1.49l.25.72c.15.44.02.92-.33 1.23l-.58.5a1.14 1.14 0 0 0 0 1.72l.58.5c.35.3.48.79.33 1.23l-.25.72c-.23.66.18 1.35.85 1.49l.76.14c.45.1.8.45.9.9l.14.76c.14.67.83 1.08 1.49.85l.72-.25c.44-.15.92-.02 1.23.33l.5.58c.46.52 1.26.52 1.72 0l.5-.58c.3-.35.79-.48 1.23-.33l.72.25c.66.23 1.35-.18 1.49-.85l.14-.76c.1-.45.45-.8.9-.9l.76-.14c.67-.14 1.08-.83.85-1.49l-.25-.72c-.15-.44-.02-.92.33-1.23l.58-.5c.52-.46.52-1.26 0-1.72l-.58-.5c-.35-.3-.48-.79-.33-1.23l.25-.72a1.14 1.14 0 0 0-.85-1.49l-.76-.14c-.45-.1-.8-.45-.9-.9l-.14-.76a1.14 1.14 0 0 0-1.49-.85l-.72.25c-.44.15-.92.02-1.23-.33l-.5-.58Zm-.49 2.67L10.6 6.6c.05.15.19.24.34.25l3.26.22c.36.03.5.48.23.71l-2.5 2.1a.4.4 0 0 0-.14.4l.8 3.16a.4.4 0 0 1-.6.44L9.2 12.13a.4.4 0 0 0-.42 0l-2.77 1.74a.4.4 0 0 1-.6-.44l.8-3.16a.4.4 0 0 0-.13-.4l-2.5-2.1a.4.4 0 0 1 .22-.7l3.26-.23a.4.4 0 0 0 .34-.25l1.22-3.03a.4.4 0 0 1 .74 0Z"></path></svg>            <span class="-link--channel-name">Explore Collectives</span>
    </a>
</li>

                    </ol>
                </li>
                   


<li>
    <ol class="nav-links">
                

<li class="js-freemium-cta ps-relative">

    <div class="fs-fine tt-uppercase ml8 mt16 mb8 fc-light">Teams</div>

    <div class="bt bl bb bc-black-075 p12 pb6 fc-black-600 blr-sm overflow-hidden">
        <strong class="fc-black-750 mb6">Stack Overflow for Teams</strong>
        – Start collaborating and sharing organizational knowledge.
        
        <img class="wmx100 mx-auto my8 h-auto d-block" width="139" height="114" src="https://cdn.sstatic.net/Img/teams/teams-illo-free-sidebar-promo.svg?v=47faa659a05e" alt="">

        <a href="https://try.stackoverflow.co/why-teams/?utm_source=so-owned&amp;utm_medium=side-bar&amp;utm_campaign=campaign-38&amp;utm_content=cta" class="w100 s-btn s-btn__primary s-btn__xs bg-orange-400 js-gps-track" data-gps-track="teams.create.left-sidenav.click({ Action: 6 })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams/create/free&quot;,null,null]">Create a free Team</a>
        <a href="https://stackoverflow.co/teams" class="w100 s-btn s-btn__muted s-btn__xs js-gps-track" data-gps-track="teams.create.left-sidenav.click({ Action: 5 })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">Why Teams?</a>

    </div>
</li>


            <li class="d-flex ai-center jc-space-between ml8 mt24 mb4 js-create-team-cta d-none">
                <div class="flex--item tt-uppercase fs-fine fc-light">Teams</div>
                <div class="flex--item">
                    <a href="javascript:void(0)" class="s-link p12 fc-black-500 h:fc-black-800 js-gps-track" role="button" aria-controls="popover-teams-create-cta" data-controller="s-popover" data-action="s-popover#toggle" data-s-popover-placement="bottom-start" data-s-popover-toggle-class="is-selected" data-gps-track="teams.create.left-sidenav.click({ Action: ShowInfo })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav show teams info&quot;,null,null,null]" aria-expanded="false">
                        <svg aria-hidden="true" class="svg-icon iconInfoSm" width="14" height="14" viewBox="0 0 14 14"><path d="M7 1a6 6 0 1 1 0 12A6 6 0 0 1 7 1Zm1 10V6H6v5h2Zm0-6V3H6v2h2Z"></path></svg>
                    </a>

                </div>
            </li>
            <li class="ps-relative js-create-team-cta d-none">
                <a href="https://stackoverflowteams.com/teams/create/free?utm_source=so-owned&amp;utm_medium=side-bar&amp;utm_campaign=campaign-38&amp;utm_content=cta" class="pl8 js-gps-track nav-links--link" title="Stack Overflow for Teams is a private, secure spot for your organization's questions and answers." data-gps-track="teams.create.left-sidenav.click({ Action: FreemiumTeamsCreateClick })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav team click&quot;,&quot;stackoverflow.com/teams/create/free&quot;,null,null]">
                    <div class="d-flex ai-center">
                        <div class="flex--item s-avatar va-middle bg-orange-400">
                            <div class="s-avatar--letter mtn1">
                                <svg aria-hidden="true" class="svg-icon iconBriefcaseSm" width="14" height="14" viewBox="0 0 14 14"><path d="M4 3a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v1h.5c.83 0 1.5.67 1.5 1.5v5c0 .83-.67 1.5-1.5 1.5h-7A1.5 1.5 0 0 1 2 10.5v-5C2 4.67 2.67 4 3.5 4H4V3Zm5 1V3H5v1h4Z"></path></svg>
                            </div>
                            <svg aria-hidden="true" class="native s-avatar--badge svg-icon iconShieldXSm" width="9" height="10" viewBox="0 0 9 10"><path d="M0 1.84 4.5 0 9 1.84v3.17C9 7.53 6.3 10 4.5 10 2.7 10 0 7.53 0 5.01V1.84Z" fill="var(--white)"></path><path d="M1 2.5 4.5 1 8 2.5v2.51C8 7.34 5.34 9 4.5 9 3.65 9 1 7.34 1 5.01V2.5Zm2.98 3.02L3.2 7h2.6l-.78-1.48a.4.4 0 0 1 .15-.38c.34-.24.73-.7.73-1.14 0-.71-.5-1.23-1.41-1.23-.92 0-1.39.52-1.39 1.23 0 .44.4.9.73 1.14.12.08.18.23.15.38Z" fill="var(--black-500)"></path></svg>
                        </div>
                        <div class="flex--item pl6">
                            Create free Team
                        </div>
                    </div>
                </a>
            </li>
    </ol>
</li>
            </ol>
        </nav>
    </div>


        <div class="s-popover ws2" id="popover-discover-collectives" role="menu">
            <div class="s-popover--arrow"></div>
            <div>
                <svg aria-hidden="true" class="fc-orange-500 float-right ml24 svg-spot spotCollective" width="48" height="48" viewBox="0 0 48 48"><path d="M25.5 7a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5ZM14 18.25c0-.69.56-1.25 1.25-1.25h22.5c.69 0 1.25.56 1.25 1.25V37.5a1 1 0 0 1-1.6.8l-4.07-3.05a1.25 1.25 0 0 0-.75-.25H15.25c-.69 0-1.25-.56-1.25-1.25v-15.5ZM7 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0ZM25.5 48a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5ZM48 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0Z" opacity=".2"></path><path d="M21 3.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0ZM24.5 2a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3ZM0 23.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0ZM3.5 22a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3ZM21 44.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0Zm3.5-1.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Zm20-23a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7ZM43 23.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm-23.23-3.14a1 1 0 0 1-.13 1.4l-2.08 1.74 2.08 1.73a1 1 0 1 1-1.28 1.54l-2.42-2.02a1.63 1.63 0 0 1 0-2.5l2.42-2.02a1 1 0 0 1 1.4.13Zm7.59 1.41a1 1 0 1 1 1.28-1.54l2.42 2.02c.78.65.78 1.85 0 2.5l-2.42 2.02a1 1 0 1 1-1.28-1.54l2.08-1.73-2.08-1.73ZM24.12 18a1 1 0 0 1 .87 1.12l-1 8a1 1 0 1 1-1.98-.24l1-8a1 1 0 0 1 1.11-.87Zm-11.87-5C11.01 13 10 14 10 15.25v15.5c0 1.24 1 2.25 2.25 2.25h17.33c.06 0 .11.02.15.05l4.07 3.05a2 2 0 0 0 3.2-1.6V15.25c0-1.24-1-2.25-2.25-2.25h-22.5ZM12 15.25c0-.14.11-.25.25-.25h22.5c.14 0 .25.11.25.25V34.5l-4.07-3.05a2.2 2.2 0 0 0-1.35-.45H12.25a.25.25 0 0 1-.25-.25v-15.5Zm7.24-10.68a1 1 0 1 0-.48-1.94A22.04 22.04 0 0 0 2.91 17.7a1 1 0 1 0 1.92.58 20.04 20.04 0 0 1 14.4-13.72Zm11.05-1.66a1 1 0 0 0-.58 1.92c6.45 1.92 11.54 7 13.46 13.46a1 1 0 1 0 1.92-.58 22.05 22.05 0 0 0-14.8-14.8ZM4.57 28.76a1 1 0 0 0-1.94.48 22.03 22.03 0 0 0 16.13 16.13 1 1 0 1 0 .48-1.94A20.03 20.03 0 0 1 4.57 28.76Zm40.8.48a1 1 0 1 0-1.94-.48 20.04 20.04 0 0 1-13.72 14.41 1 1 0 0 0 .58 1.92 22.04 22.04 0 0 0 15.08-15.85Z"></path></svg>
                <h5 class="pt4 fw-bold">Collectives™ on Stack Overflow</h5>
                <p class="my16 fs-caption fc-medium">Find centralized, trusted content and collaborate around the technologies you use most.</p>
                <a href="/collectives" class="js-gps-track s-btn s-btn__primary s-btn__xs" data-gps-track="top_nav.click({is_current:false, location:2, destination:18})">
                    Learn more about Collectives
                </a>
            </div>
        </div>


        <div class="s-popover ws2" id="popover-teams-create-cta" role="menu" aria-hidden="true">
            <div class="s-popover--arrow"></div>

            <div class="ps-relative overflow-hidden">
                <p class="mb2"><strong>Teams</strong></p>
                <p class="mb12 fs-caption fc-black-400">Q&amp;A for work</p>
                <p class="mb12 fs-caption fc-medium">Connect and share knowledge within a single location that is structured and easy to search.</p>
                <a href="https://stackoverflow.co/teams" class="js-gps-track s-btn s-btn__primary s-btn__xs" data-gps-track="teams.create.left-sidenav.click({ Action: CtaClick })" data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">
                    Learn more about Teams
                </a>
            </div>

            <div class="ps-absolute t8 r8">
                <svg aria-hidden="true" class="fc-orange-500 svg-spot spotPeople" width="48" height="48" viewBox="0 0 48 48"><path d="M13.5 28a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM7 30a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v5h11v-5a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v10a2 2 0 0 1-2 2H33v5a1 1 0 0 1-1 1H20a1 1 0 0 1-1-1v-5H8a1 1 0 0 1-1-1V30Zm25-6.5a4.5 4.5 0 1 0 9 0 4.5 4.5 0 0 0-9 0ZM24.5 34a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9Z" opacity=".2"></path><path d="M16.4 26.08A6 6 0 1 0 7.53 26C5.64 26.06 4 27.52 4 29.45V40a1 1 0 0 0 1 1h9a1 1 0 1 0 0-2h-4v-7a1 1 0 1 0-2 0v7H6v-9.55c0-.73.67-1.45 1.64-1.45H16a1 1 0 0 0 .4-1.92ZM12 18a4 4 0 1 1 0 8 4 4 0 0 1 0-8Zm16.47 14a6 6 0 1 0-8.94 0A3.6 3.6 0 0 0 16 35.5V46a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V35.5c0-1.94-1.64-3.42-3.53-3.5ZM20 28a4 4 0 1 1 8 0 4 4 0 0 1-8 0Zm-.3 6h8.6c1 0 1.7.75 1.7 1.5V45h-2v-7a1 1 0 1 0-2 0v7h-4v-7a1 1 0 1 0-2 0v7h-2v-9.5c0-.75.7-1.5 1.7-1.5ZM42 22c0 1.54-.58 2.94-1.53 4A3.5 3.5 0 0 1 44 29.45V40a1 1 0 0 1-1 1h-9a1 1 0 1 1 0-2h4v-7a1 1 0 1 1 2 0v7h2v-9.55A1.5 1.5 0 0 0 40.48 28H32a1 1 0 0 1-.4-1.92A6 6 0 1 1 42 22Zm-2 0a4 4 0 1 0-8 0 4 4 0 0 0 8 0Z"></path><g opacity=".35"><path d="M17 10a1 1 0 011-1h12a1 1 0 110 2H18a1 1 0 01-1-1Zm1-5a1 1 0 100 2h12a1 1 0 100-2H18ZM14 1a1 1 0 00-1 1v12a1 1 0 001 1h5.09l4.2 4.2a1 1 0 001.46-.04l3.7-4.16H34a1 1 0 001-1V2a1 1 0 00-1-1H14Zm1 12V3h18v10h-5a1 1 0 00-.75.34l-3.3 3.7-3.74-3.75a1 1 0 00-.71-.29H15Z"></path></g></svg>
            </div>
        </div>


</div>






        <div id="content" class="snippet-hidden">

            

<div itemprop="mainEntity" itemscope="" itemtype="https://schema.org/Question">
    <link itemprop="image" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">

    <div class="inner-content clearfix">

        

            <div id="question-header" class="d-flex sm:fd-column">
                        <h1 itemprop="name" class="fs-headline1 ow-break-word mb8 flex--item fl1"><a href="/questions/9688200/difference-between-shared-objects-so-static-libraries-a-and-dlls-so" class="question-hyperlink">Difference between shared objects (.so), static libraries (.a), and DLL's (.so)?</a></h1>
                <div class="ml12 aside-cta flex--item print:d-none sm:ml0 sm:mb12 sm:order-first sm:as-end">
                        <a href="/questions/ask" class="ws-nowrap s-btn s-btn__primary">
        Ask Question
    </a>

                </div>
            </div>
            <div class="d-flex fw-wrap pb8 mb16 bb bc-black-075">
                    <div class="flex--item ws-nowrap mr16 mb8" title="2012-03-13 16:37:53Z">
                        <span class="fc-light mr2">Asked</span>
                        <time itemprop="dateCreated" datetime="2012-03-13T16:37:53">10 years, 9 months ago</time>
                    </div>
                    <div class="flex--item ws-nowrap mr16 mb8">
                        <span class="fc-light mr2">Modified</span>
                        <a href="?lastactivity" class="s-link s-link__inherit" title="2022-02-20 04:39:42Z">10 months ago</a>
                    </div>
                    <div class="flex--item ws-nowrap mb8" title="Viewed 212,320 times">
                        <span class="fc-light mr2">Viewed</span>
                        212k times
                    </div>
            </div>
            <div id="mainbar" role="main" aria-label="question and answers">

                
<div class="question js-question" data-questionid="9688200" data-position-on-page="0" data-score="352" id="question">
    <style>
    </style>
<div class="js-zone-container zone-container-main">
    <div id="dfp-tlb" class="everyonelovesstackoverflow everyoneloves__top-leaderboard everyoneloves__leaderboard" data-dfp-zone="true" style="min-height: auto; height: auto;" data-google-query-id="CKryor6EkPwCFbjh_QUdg6YMtQ"><div id="google_ads_iframe_/248424177/stackoverflow.com/lb/question-pages_0__container__" style="border: 0pt none; display: inline-block; width: 728px; height: 90px;"><iframe frameborder="0" src="https://6069a9ccde7913e3c1d8e794842d62f0.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html" id="google_ads_iframe_/248424177/stackoverflow.com/lb/question-pages_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="728" height="90" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" role="region" aria-label="Advertisement" tabindex="0" data-google-container-id="1" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div></div>
		<div class="js-report-ad-button-container " style="width: 728px; height: 24px;"><button data-google-event-data="{&quot;serviceName&quot;:&quot;publisher_ads&quot;,&quot;slot&quot;:{},&quot;isEmpty&quot;:false,&quot;slotContentChanged&quot;:true,&quot;size&quot;:[728,90],&quot;advertiserId&quot;:4933108035,&quot;campaignId&quot;:2945342793,&quot;creativeId&quot;:138414988574,&quot;creativeTemplateId&quot;:null,&quot;labelIds&quot;:null,&quot;lineItemId&quot;:5847406694,&quot;sourceAgnosticCreativeId&quot;:138414988574,&quot;sourceAgnosticLineItemId&quot;:5847406694,&quot;isBackfill&quot;:false,&quot;yieldGroupIds&quot;:null,&quot;companyIds&quot;:null}" data-modal-url="/ads/report-ad" data-ad-unit="dfp-tlb" class="js-report-ad s-btn s-btn__link fs-fine mt2 float-right">Report this ad</button></div>
</div>

    <div class="post-layout ">
        <div class="votecell post-layout--left">
            <div class="js-voting-container d-flex jc-center fd-column ai-stretch gs4 fc-black-200" data-post-id="9688200">
        <button class="js-vote-up-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-cchc5trd">
            <svg aria-hidden="true" class="svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 25h32L18 9 2 25Z"></path></svg>
        </button><div id="--stacks-s-tooltip-cchc5trd" class="s-popover s-popover__tooltip" role="tooltip">This question shows research effort; it is useful and clear<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title" itemprop="upvoteCount" data-value="352">
            352
        </div>
        <button class="js-vote-down-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-aqk4jftn">
            <svg aria-hidden="true" class="svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 11h32L18 27 2 11Z"></path></svg>
        </button><div id="--stacks-s-tooltip-aqk4jftn" class="s-popover s-popover__tooltip" role="tooltip">This question does not show any research effort; it is unclear or not useful<div class="s-popover--arrow"></div></div>


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" id="saves-btn-9688200" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" aria-pressed="false" data-post-id="9688200" data-post-type-id="1" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-m8wcstxn">
    <svg aria-hidden="true" class="fc-theme-primary-500 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26l4-2.66ZM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
</button><div id="--stacks-s-tooltip-m8wcstxn" class="s-popover s-popover__tooltip" role="tooltip">Save this question.<div class="s-popover--arrow"></div></div>








    
        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/9688200/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-g7d5nbop"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"></path></svg></a><div id="--stacks-s-tooltip-g7d5nbop" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="postcell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
                
<p>I have been involved in some debate with respect to libraries in Linux, and would like to confirm some things.</p>
<p>It is to my understanding (please correct me if I am wrong and I will edit my post later), that there are two ways of using libraries when building an application:</p>
<ol>
<li>Static libraries (.a files): At link time, a copy of the entire library is put into the final application so that the functions within the library are always available to the calling application</li>
<li>Shared objects (.so files): At link time, the object is just verified against its API via the corresponding header (.h) file. The library isn't actually used until runtime, where it is needed.</li>
</ol>
<p>The obvious advantage of static libraries is that they allow the entire application to be self-contained, while the benefit of dynamic libraries is that the ".so" file can be replaced (ie: in case it needs to be updated due to a security bug) without requiring the base application to be recompiled.</p>
<p>I have heard some people make a distinction between shared objects and dynamic link libraries (DLL's), even though they are both ".so" files. Is there any distinction between shared objects and DLLs when it comes to C/C++ development on Linux or any other POSIX compliant OS (ie: MINIX, UNIX, QNX, etc)? I am told that one key difference (so far) is that shared objects are just used at runtime, while DLL's must be opened first using the dlopen() call within the application.</p>
<p>Finally, I have also heard some developers mention "shared archives", which, to my understanding, are also static libraries themselves, but are never used by an application directly. Instead, other static libraries will link against the "shared archives" to pull some (but not all) functions/resources from the shared archive into the static library being built.</p>
<p>Thank you all in advance for your assistance.</p>
<h1>Update</h1>
<hr>
<p><strong>In the context in which these terms were provided to me, it was effectively erroneous terms used by a team of Windows developers that had to learn Linux. I tried to correct them, but the (incorrect) language norms stuck.</strong></p>
<ol>
<li>Shared Object: A library that is automatically linked into a program when the program starts, and exists as a standalone file. The library is included in the linking list at compile time (ie: <code>LDOPTS+=-lmylib</code> for a library file named <code>mylib.so</code>). <strong>The library must be present at compile time, and when the application starts.</strong></li>
<li>Static Library: A library that is merged into the actual program itself at build time for a single (larger) application containing the application code and the library code that is automatically linked into a program when the program is built, and the final binary containing both the main program and the library itself exists as a single standalone binary file. The library is included in the linking list at compile time (ie: <code>LDOPTS+=-lmylib</code> for a library file named <code>mylib.a</code>). <strong>The library must be present at compile time.</strong></li>
<li>DLL: Essentially the same as a shared object, but rather than being included in the linking list at compile time, the library is loaded via <code>dlopen()</code>/<code>dlsym()</code> commands so that the library does not need to be present at build time for the program to compile. <strong>Also, the library does not need to be present (necessarily) at application startup or compile time</strong>, as it is only needed at the moment the <code>dlopen</code>/<code>dlsym</code> calls are made.</li>
<li>Shared Archive: Essentially the same as a static library, but is compiled with the "export-shared" and "<code>-fPIC</code>" flags. The library is included in the linking list at compile time (ie: <code>LDOPTS+=-lmylibS</code> for a library file named <code>mylibS.a</code>). The distinction between the two is that this additional flag is required if a shared object or DLL wants to statically link the shared archive into its own code AND be able to make the functions in the shared object available to other programs, rather than just using them internal to the DLL. This is useful in the case when someone provides you with a static library, and you wish to repackage it as an SO. <strong>The library must be present at compile time.</strong></li>
</ol>
<h1>Additional Update</h1>
<p>The distinction between "<code>DLL</code>" and "<code>shared library</code>" was just a (lazy, inaccurate) colloquialism in the company I worked in at the time (Windows developers being forced to shift to Linux development, and the term stuck), adhering to the descriptions noted above.</p>
<p>Additionally, the trailing "<code>S</code>" literal after the library name, in the case of "shared archives" was just a convention used at that company, and not in the industry in general.</p>
    </div>

        <div class="mt24 mb12">
            <div class="post-taglist d-flex gs4 gsy fd-column">
                <div class="d-flex ps-relative fw-wrap">
                    <ul class="ml0 list-ls-none js-post-tag-list-wrapper d-inline"><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/c%2b%2b" class="post-tag" title="show questions tagged 'c++'" aria-label="show questions tagged 'c++'" rel="tag" aria-labelledby="c++-container">c++</a></li><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/c" class="post-tag" title="show questions tagged 'c'" aria-label="show questions tagged 'c'" rel="tag" aria-labelledby="c-container">c</a></li><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/linux" class="post-tag" title="show questions tagged 'linux'" aria-label="show questions tagged 'linux'" rel="tag" aria-labelledby="linux-container">linux</a></li><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/dll" class="post-tag" title="show questions tagged 'dll'" aria-label="show questions tagged 'dll'" rel="tag" aria-labelledby="dll-container">dll</a></li><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/linker" class="post-tag" title="show questions tagged 'linker'" aria-label="show questions tagged 'linker'" rel="tag" aria-labelledby="linker-container">linker</a></li></ul>
                </div>
            </div>
        </div>

    <div class="mb0 ">
        <div class="mt16 d-flex gs8 gsy fw-wrap jc-end ai-start pt4 mb16">
            <div class="flex--item mr16 fl1 w96">
                


<div class="js-post-menu pt2" data-post-id="9688200">
    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

            <div class="flex--item">
                <a href="/q/9688200" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this question" data-gps-track="post.click({ item: 2, priv: 0, post_type: 1 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this question" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="question" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="1" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f4.0%2f" data-se-share-sheet-license-name="CC BY-SA 4.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-0" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-0"><div class="s-popover--arrow"></div><div><label class="js-title fw-bold" for="share-sheet-input-se-share-sheet-0">Share a link to this question</label> <span class="js-subtitle"></span></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-0" class="js-input s-input wmn3 sm:wmn-initial bc-black-200 bg-white fc-dark" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 4.0">CC BY-SA 4.0</a><div class="js-social-container d-none"></div></div></div>
            </div>


                    <div class="flex--item">
                        <a href="/posts/9688200/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 1 })" title="">Improve this question</a>
                    </div>

            <div class="flex--item">
                <button type="button" id="btnFollowPost-9688200" class="s-btn s-btn__link js-follow-post js-follow-question js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 1 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-7aha8ycz">
                    Follow
                </button><div id="--stacks-s-tooltip-7aha8ycz" class="s-popover s-popover__tooltip" role="tooltip">Follow this question to receive notifications<div class="s-popover--arrow"></div></div>
            </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>

                <div class="post-signature flex--item">
<div class="user-info user-hover">
    <div class="user-action-time">
        <a href="/posts/9688200/revisions" title="show all edits to this post" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 1 })">edited <span title="2022-02-20 04:39:42Z" class="relativetime">Feb 20 at 4:39</span></a>
    </div>
    <div class="user-gravatar32">
        <a href="/users/5277849/nixalott"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/80c6ccf8443397457d441661201d7538?s=64&amp;d=identicon&amp;r=PG" alt="nixalott's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details">
        <a href="/users/5277849/nixalott">nixalott</a>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">15</span><span title="5 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">5</span></span><span class="v-visible-sr">5 bronze badges</span>
        </div>
    </div>
</div>
                </div>
            <div class="post-signature owner flex--item">
                <div class="user-info ">
    <div class="user-action-time">
        asked <span title="2012-03-13 16:37:53Z" class="relativetime">Mar 13, 2012 at 16:37</span>
    </div>
    <div class="user-gravatar32">
        <a href="/users/1022889/cloud"><div class="gravatar-wrapper-32"><img src="https://i.stack.imgur.com/WZOSZ.jpg?s=64&amp;g=1" alt="Cloud's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/1022889/cloud">Cloud</a><span class="d-none" itemprop="name">Cloud</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score 18,393" dir="ltr">18.4k</span><span title="15 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">15</span></span><span class="v-visible-sr">15 gold badges</span><span title="76 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">76</span></span><span class="v-visible-sr">76 silver badges</span><span title="149 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">149</span></span><span class="v-visible-sr">149 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
    </div>
    
</div>




            <span class="d-none" itemprop="commentCount">8</span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-9688200" class="comments js-comments-container bt bc-black-075 mt12 " data-post-id="9688200" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="3" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-12310351" class="comment js-comment " data-comment-id="12310351" data-comment-owner-id="440558" data-comment-score="19">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="hot">19</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">For <code>.a</code> files, the "a" actually stands for "archove", and it's simply an archive of object files. Modern linkers should be good enough to not need to include the while library, just the objects files in the archive that is needed, and might even just use the sections of code/data in the object files that are referenced.</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/440558/some-programmer-dude" title="390,902 reputation" class="comment-user">Some programmer dude</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12310351_9688200" aria-label="Link to comment"><span title="2012-03-13 16:47:53Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 16:47</span></a></span>
                        <span title="this comment was edited 1 time">
                            <svg aria-hidden="true" class="va-text-bottom o50 svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0ZM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88Z"></path></svg>
                        </span>
            </div>
        </div>
    </li>
    <li id="comment-12310538" class="comment js-comment " data-comment-id="12310538" data-comment-owner-id="379897" data-comment-score="6">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="warm">6</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">DLL is just Windows terminology. It's not used on unices.</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/379897/r-github-stop-helping-ice" title="205,034 reputation" class="comment-user">R.. GitHub STOP HELPING ICE</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12310538_9688200" aria-label="Link to comment"><span title="2012-03-13 16:53:52Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 16:53</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-12310769" class="comment js-comment " data-comment-id="12310769" data-comment-owner-id="140367" data-comment-score="2">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">2</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">possible duplicate of <a href="http://stackoverflow.com/questions/6181078/why-are-static-and-dynamic-linkable-libraries-different">Why are static and dynamic linkable libraries different?</a></span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/140367/tam%c3%a1s-szelei" title="22,559 reputation" class="comment-user">Tamás Szelei</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12310769_9688200" aria-label="Link to comment"><span title="2012-03-13 17:02:03Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 17:02</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-12311452" class="comment js-comment " data-comment-id="12311452" data-comment-owner-id="841108" data-comment-score="3">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">3</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">Read <a href="http://tldp.org/HOWTO/Program-Library-HOWTO/" rel="nofollow noreferrer">tldp.org/HOWTO/Program-Library-HOWTO</a></span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/841108/basile-starynkevitch" title="1 reputation" class="comment-user">Basile Starynkevitch</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12311452_9688200" aria-label="Link to comment"><span title="2012-03-13 17:30:19Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 17:30</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-79854303" class="comment js-comment " data-comment-id="79854303" data-comment-owner-id="440558" data-comment-score="7">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="warm">7</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">@DevNull "arch<b>i</b>ve" of course. :)</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/440558/some-programmer-dude" title="390,902 reputation" class="comment-user">Some programmer dude</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment79854303_9688200" aria-label="Link to comment"><span title="2017-09-27 13:36:49Z, License: CC BY-SA 3.0" class="relativetime-clean">Sep 27, 2017 at 13:36</span></a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-9688200" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link dno" title="Use comments to ask for more information or suggest improvements. Avoid answering questions in comments." href="#" role="button"></a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link " title="Expand to show all comments on this post" href="#" onclick="" role="button">Show <b>3</b> more comments</a>
        </div>         
    </div>
    </div>

</div>


<div class="js-zone-container zone-container-responsive">
    <div id="dfp-isb" class="everyonelovesstackoverflow everyoneloves__inline-sidebar mx-auto" style="min-height: auto; height: auto; display: none;"></div>
		<div class="js-report-ad-button-container mx-auto" style="width: 300px"></div>
</div>

                <div id="answers">
                    <a name="tab-top"></a>
                    <div id="answers-header">
                        <div class="answers-subheader d-flex ai-center mb8">
                            <div class="flex--item fl1">
                                <h2 class="mb0" data-answercount="5">
                                        5 Answers
                                    <span style="display:none;" itemprop="answerCount">5</span>
                                </h2>
                            </div>
                            <div class="flex--item">
                                

<div class="d-flex g4 gsx ai-center sm:fd-column sm:ai-start">
    <div class="d-flex fd-column ai-end sm:ai-start">
        <label class="flex--item fs-caption" for="answer-sort-dropdown-select-menu">
            Sorted by:
        </label>
        <a class="js-sort-preference-change s-link flex--item fs-fine d-none" data-value="ScoreDesc" href="/questions/9688200/difference-between-shared-objects-so-static-libraries-a-and-dlls-so?answertab=scoredesc#tab-top">
            Reset to default
        </a>
    </div>
    <div class="flex--item s-select">
        <select id="answer-sort-dropdown-select-menu">
                    <option value="scoredesc" selected="selected">
                        Highest score (default)
                    </option>
                    <option value="trending">
                        Trending (recent votes count more)
                    </option>
                    <option value="modifieddesc">
                        Date modified (newest first)
                    </option>
                    <option value="createdasc">
                        Date created (oldest first)
                    </option>
        </select>
    </div>
</div>


                            </div>
                        </div>
                            
                    </div>


                                        
<a name="9688536"></a>
<div id="answer-9688536" class="answer js-answer" data-answerid="9688536" data-parentid="9688200" data-score="258" data-position-on-page="1" data-highest-scored="1" data-question-has-accepted-highest-score="0" itemprop="acceptedAnswer" itemscope="" itemtype="https://schema.org/Answer">
    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container d-flex jc-center fd-column ai-stretch gs4 fc-black-200" data-post-id="9688536">
        <button class="js-vote-up-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-6m9qko6v">
            <svg aria-hidden="true" class="svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 25h32L18 9 2 25Z"></path></svg>
        </button><div id="--stacks-s-tooltip-6m9qko6v" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title" itemprop="upvoteCount" data-value="258">
            258
        </div>
        <button class="js-vote-down-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-rij4gmwy">
            <svg aria-hidden="true" class="svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 11h32L18 27 2 11Z"></path></svg>
        </button><div id="--stacks-s-tooltip-rij4gmwy" class="s-popover s-popover__tooltip" role="tooltip">This answer is not useful<div class="s-popover--arrow"></div></div>


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" id="saves-btn-9688536" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" aria-pressed="false" data-post-id="9688536" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-w2tzuxm2">
    <svg aria-hidden="true" class="fc-theme-primary-500 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26l4-2.66ZM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
</button><div id="--stacks-s-tooltip-w2tzuxm2" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-700 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8v-8Z"></path></svg>
                </div>
            </div>

    
        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/9688536/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-mp8shsrl"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"></path></svg></a><div id="--stacks-s-tooltip-mp8shsrl" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>A <strong>static library(.a)</strong> is a library that can be linked directly into the final executable produced by the linker,it is contained in it and there is no need to have the library into the system where the executable will be deployed.</p>

<p>A <strong>shared library(.so)</strong> is a library that is linked but not embedded in the final executable, so will be loaded when the executable is launched and need to be present in the system where the executable is deployed.</p>

<p>A <strong>dynamic link library on windows(.dll)</strong> is like a shared library(.so) on linux but there are some differences between the two implementations that are related to the OS (Windows vs Linux) : </p>

<p>A <strong>DLL</strong> can define two kinds of functions: exported and internal. The exported functions are intended to be called by other modules, as well as from within the DLL where they are defined. Internal functions are typically intended to be called only from within the DLL where they are defined. </p>

<p>An <strong>SO</strong> library on Linux doesn't need special export statement to indicate exportable symbols, since all symbols are available to an interrogating process.</p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2012-03-13T16:58:43"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="9688536">
    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

            <div class="flex--item">
                <a href="/a/9688536" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-1" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-1"><div class="s-popover--arrow"></div><div><label class="js-title fw-bold" for="share-sheet-input-se-share-sheet-1">Share a link to this answer</label> <span class="js-subtitle"></span></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-1" class="js-input s-input wmn3 sm:wmn-initial bc-black-200 bg-white fc-dark" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container d-none"></div></div></div>
            </div>


                    <div class="flex--item">
                        <a href="/posts/9688536/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

            <div class="flex--item">
                <button type="button" id="btnFollowPost-9688536" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-83vc4s7o">
                    Follow
                </button><div id="--stacks-s-tooltip-83vc4s7o" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
            </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info user-hover">
    <div class="user-action-time">
        answered <span title="2012-03-13 16:58:43Z" class="relativetime">Mar 13, 2012 at 16:58</span>
    </div>
    <div class="user-gravatar32">
        <a href="/users/330280/aleroot"><div class="gravatar-wrapper-32"><img src="https://i.stack.imgur.com/ciT71.png?s=64&amp;g=1" alt="aleroot's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/330280/aleroot">aleroot</a><span class="d-none" itemprop="name">aleroot</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score 69,887" dir="ltr">69.9k</span><span title="30 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">30</span></span><span class="v-visible-sr">30 gold badges</span><span title="173 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">173</span></span><span class="v-visible-sr">173 silver badges</span><span title="210 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">210</span></span><span class="v-visible-sr">210 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




            <span class="d-none" itemprop="commentCount">3</span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-9688536" class="comments js-comments-container bt bc-black-075 mt12 " data-post-id="9688536" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-21550983" class="comment js-comment " data-comment-id="21550983" data-comment-owner-id="1348709" data-comment-score="3">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">3</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">+1 nice simple explanation. If a function is declared "Internal" in a DLL does that mean it <i>can't</i> be called from outside the library?</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/1348709/mike" title="45,643 reputation" class="comment-user">Mike</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment21550983_9688536" aria-label="Link to comment"><span title="2013-03-07 16:03:00Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 7, 2013 at 16:03</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-22278092" class="comment js-comment " data-comment-id="22278092" data-comment-owner-id="13422" data-comment-score="33">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="supernova">33</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">It is not necessarily true that all symbols are available in a SO library. Hidden symbols are possible and recommended because there is no good reason for library users to see all of your symbols.</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/13422/zan-lynx" title="52,005 reputation" class="comment-user">Zan Lynx</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment22278092_9688536" aria-label="Link to comment"><span title="2013-03-28 19:25:25Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 28, 2013 at 19:25</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-38265026" class="comment js-comment " data-comment-id="38265026" data-comment-owner-id="84661" data-comment-score="7">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="warm">7</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">FYI: g++ has <code>__attribute__</code> syntax for selectively 'export' symbols: <code>#define DLLEXPORT __attribute__ ((visibility("default")))</code> <code>#define DLLLOCAL   __attribute__ ((visibility("hidden")))</code></span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/84661/brian-cannard" title="842 reputation" class="comment-user">Brian Cannard</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment38265026_9688536" aria-label="Link to comment"><span title="2014-07-10 14:49:59Z, License: CC BY-SA 3.0" class="relativetime-clean">Jul 10, 2014 at 14:49</span></a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-9688536" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>         
    </div>
    </div>
</div>

<div class="js-zone-container zone-container-main">
    <div id="dfp-mlb" class="everyonelovesstackoverflow everyoneloves__mid-leaderboard everyoneloves__leaderboard" style="min-height: auto; height: auto; display: none;" data-google-query-id="CKKLpb6EkPwCFRvh_QUdKdELRw"><div id="google_ads_iframe_/248424177/stackoverflow.com/mlb/question-pages_0__container__" style="border: 0pt none; width: 728px; height: 0px;"></div></div>
		<div class="js-report-ad-button-container " style="width: 728px"></div>
</div>
                                        
<a name="9688338"></a>
<div id="answer-9688338" class="answer js-answer accepted-answer js-accepted-answer" data-answerid="9688338" data-parentid="9688200" data-score="120" data-position-on-page="2" data-highest-scored="0" data-question-has-accepted-highest-score="0" itemprop="suggestedAnswer" itemscope="" itemtype="https://schema.org/Answer">
    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container d-flex jc-center fd-column ai-stretch gs4 fc-black-200" data-post-id="9688338">
        <button class="js-vote-up-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-z4febq4j">
            <svg aria-hidden="true" class="svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 25h32L18 9 2 25Z"></path></svg>
        </button><div id="--stacks-s-tooltip-z4febq4j" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title" itemprop="upvoteCount" data-value="120">
            120
        </div>
        <button class="js-vote-down-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-hvytus3m">
            <svg aria-hidden="true" class="svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 11h32L18 27 2 11Z"></path></svg>
        </button><div id="--stacks-s-tooltip-hvytus3m" class="s-popover s-popover__tooltip" role="tooltip">This answer is not useful<div class="s-popover--arrow"></div></div>


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" id="saves-btn-9688338" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" aria-pressed="false" data-post-id="9688338" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-o0bm8mlz">
    <svg aria-hidden="true" class="fc-theme-primary-500 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26l4-2.66ZM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
</button><div id="--stacks-s-tooltip-o0bm8mlz" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-700 py6 mtn8" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8v-8Z"></path></svg>
                </div>
            </div>

    
        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/9688338/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-f6nrtftb"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"></path></svg></a><div id="--stacks-s-tooltip-f6nrtftb" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>I've always thought that DLLs and shared objects are just different terms for the same thing - Windows calls them DLLs, while on UNIX systems they're shared objects, with the general term - dynamically linked library - covering both (even the function to open a .so on UNIX is called <code>dlopen()</code> after 'dynamic library').</p>

<p>They are indeed only linked at application startup, however your notion of verification against the header file is incorrect. The header file defines prototypes which are required in order to compile the code which uses the library, but at link time the linker looks inside the library itself to make sure the functions it needs are actually there. The linker has to find the function bodies somewhere at link time or it'll raise an error. It ALSO does that at runtime, because as you rightly point out the library itself might have changed since the program was compiled. This is why ABI stability is so important in platform libraries, as the ABI changing is what breaks existing programs compiled against older versions.</p>

<p>Static libraries are just bundles of object files straight out of the compiler, just like the ones that you are building yourself as part of your project's compilation, so they get pulled in and fed to the linker in exactly the same way, and unused bits are dropped in exactly the same way.</p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2012-03-13T16:45:32"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="9688338">
    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

            <div class="flex--item">
                <a href="/a/9688338" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-2" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-2"><div class="s-popover--arrow"></div><div><label class="js-title fw-bold" for="share-sheet-input-se-share-sheet-2">Share a link to this answer</label> <span class="js-subtitle"></span></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-2" class="js-input s-input wmn3 sm:wmn-initial bc-black-200 bg-white fc-dark" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container d-none"></div></div></div>
            </div>


                    <div class="flex--item">
                        <a href="/posts/9688338/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

            <div class="flex--item">
                <button type="button" id="btnFollowPost-9688338" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-oe9q9z7c">
                    Follow
                </button><div id="--stacks-s-tooltip-oe9q9z7c" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
            </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info user-hover">
    <div class="user-action-time">
        answered <span title="2012-03-13 16:45:32Z" class="relativetime">Mar 13, 2012 at 16:45</span>
    </div>
    <div class="user-gravatar32">
        <a href="/users/241544/matthew-walton"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/d27ca4e9a9a41ec8732046e6a272f091?s=64&amp;d=identicon&amp;r=PG" alt="Matthew Walton's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/241544/matthew-walton">Matthew Walton</a><span class="d-none" itemprop="name">Matthew Walton</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">9,639</span><span title="3 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">3</span></span><span class="v-visible-sr">3 gold badges</span><span title="27 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">27</span></span><span class="v-visible-sr">27 silver badges</span><span title="36 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">36</span></span><span class="v-visible-sr">36 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




            <span class="d-none" itemprop="commentCount">8</span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-9688338" class="comments js-comments-container bt bc-black-075 mt12 " data-post-id="9688338" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="3" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-12310338" class="comment js-comment " data-comment-id="12310338" data-comment-owner-id="1022889" data-comment-score="2">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">2</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">Why is it that some projects I see on Linux have to use the dlopen() call to access the functions within a ".so" file, and some don't have to do that at all? Thank you, by the way!</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/1022889/cloud" title="18,393 reputation" class="comment-user owner">Cloud</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12310338_9688338" aria-label="Link to comment"><span title="2012-03-13 16:47:38Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 16:47</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-12310392" class="comment js-comment " data-comment-id="12310392" data-comment-owner-id="405018" data-comment-score="11">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="warm">11</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">Those that dont do that get the functions handed to them by the process loader, ie the elf loader of linux. dlopen exists if the application wants to open and use a .so or .dll that wasnt there at compile that or just add extra functionality, like plugins.</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/405018/rapadura" title="5,114 reputation" class="comment-user">rapadura</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12310392_9688338" aria-label="Link to comment"><span title="2012-03-13 16:49:19Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 16:49</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-12310452" class="comment js-comment " data-comment-id="12310452" data-comment-owner-id="1022889" data-comment-score="1">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">1</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">But won't the application not compile at all if the .so is not present at build time? Is it possible to force the linker to just build the final program without the .so present at all? Thank you.</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/1022889/cloud" title="18,393 reputation" class="comment-user owner">Cloud</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12310452_9688338" aria-label="Link to comment"><span title="2012-03-13 16:51:08Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 16:51</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-12310547" class="comment js-comment " data-comment-id="12310547" data-comment-owner-id="405018" data-comment-score="2">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">2</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">I would believe it depends on how you use the functions from .so, but here my knowledge of this halts :/ Good questions.</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/405018/rapadura" title="5,114 reputation" class="comment-user">rapadura</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12310547_9688338" aria-label="Link to comment"><span title="2012-03-13 16:54:08Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 16:54</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-12313275" class="comment js-comment " data-comment-id="12313275" data-comment-owner-id="3805" data-comment-score="2">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">2</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">Regarding dlopen() and its family of functions, it is my understanding that this is used to programmatically open/close a dll so that it does not have to be loaded in memory throughout the whole run of the application. Otherwise, you must tell the linker in its command line arguments (aka your makefile) that you want the library loaded. It will be loaded at runtime and stay loaded in memory until the application exits. There are more things that can happen at the OS level, but this is roughly what happens as far as your application is concerned.</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/3805/taylor-price" title="622 reputation" class="comment-user">Taylor Price</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12313275_9688338" aria-label="Link to comment"><span title="2012-03-13 18:51:53Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 18:51</span></a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-9688338" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link dno" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button"></a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link " title="Expand to show all comments on this post" href="#" onclick="" role="button">Show <b>3</b> more comments</a>
        </div>         
    </div>
    </div>
</div>

                                        
<a name="23169909"></a>
<div id="answer-23169909" class="answer js-answer" data-answerid="23169909" data-parentid="9688200" data-score="47" data-position-on-page="3" data-highest-scored="0" data-question-has-accepted-highest-score="0" itemprop="suggestedAnswer" itemscope="" itemtype="https://schema.org/Answer">
    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container d-flex jc-center fd-column ai-stretch gs4 fc-black-200" data-post-id="23169909">
        <button class="js-vote-up-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-cli3tluq">
            <svg aria-hidden="true" class="svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 25h32L18 9 2 25Z"></path></svg>
        </button><div id="--stacks-s-tooltip-cli3tluq" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title" itemprop="upvoteCount" data-value="47">
            47
        </div>
        <button class="js-vote-down-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-xrjqlsiv">
            <svg aria-hidden="true" class="svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 11h32L18 27 2 11Z"></path></svg>
        </button><div id="--stacks-s-tooltip-xrjqlsiv" class="s-popover s-popover__tooltip" role="tooltip">This answer is not useful<div class="s-popover--arrow"></div></div>


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" id="saves-btn-23169909" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" aria-pressed="false" data-post-id="23169909" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-d76szkoi">
    <svg aria-hidden="true" class="fc-theme-primary-500 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26l4-2.66ZM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
</button><div id="--stacks-s-tooltip-d76szkoi" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-700 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8v-8Z"></path></svg>
                </div>
            </div>

    
        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/23169909/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-mqzo5gfi"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"></path></svg></a><div id="--stacks-s-tooltip-mqzo5gfi" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>I can elaborate on the details of DLLs in Windows to help clarify those mysteries to my friends here in *NIX-land...</p>

<p>A DLL is like a Shared Object file. Both are images, ready to load into memory by the program loader of the respective OS. The images are accompanied by various bits of metadata to help linkers and loaders make the necessary associations and use the library of code.</p>

<p>Windows DLLs have an export table. The exports can be by name, or by table position (numeric). The latter method is considered "old school" and is much more fragile -- rebuilding the DLL and changing the position of a function in the table will end in disaster, whereas there is no real issue if linking of entry points is by name. So, forget that as an issue, but just be aware it's there if you work with "dinosaur" code such as 3rd-party vendor libs.</p>

<p>Windows DLLs are built by compiling and linking, just as you would for an EXE (executable application), but the DLL is meant to not stand alone, just like an SO is meant to be used by an application, either via dynamic loading, or by link-time binding (the reference to the SO is embedded in the application binary's metadata, and the OS program loader will auto-load the referenced SO's). DLLs can reference other DLLs, just as SOs can reference other SOs.</p>

<p>In Windows, DLLs will make available only specific entry points. These are called "exports". The developer can either use a special compiler keyword to make a symbol an externally-visible (to other linkers and the dynamic loader), or the exports can be listed in a module-definition file which is used at link time when the DLL itself is being created. The modern practice is to decorate the function definition with the keyword to export the symbol name. It is also possible to create header files with keywords which will declare that symbol as one to be imported from a DLL outside the current compilation unit. Look up the keywords __declspec(dllexport) and __declspec(dllimport) for more information.</p>

<p>One of the interesting features of DLLs is that they can declare a standard "upon load/unload" handler function. Whenever the DLL is loaded or unloaded, the DLL can perform some initialization or cleanup, as the case may be. This maps nicely into having a DLL as an object-oriented resource manager, such as a device driver or shared object interface.</p>

<p>When a developer wants to use an already-built DLL, she must either reference an "export library" (*.LIB) created by the DLL developer when she created the DLL, or she must explicitly load the DLL at run time and request the entry point address by name via the LoadLibrary() and GetProcAddress() mechanisms. Most of the time, linking against a LIB file (which simply contains the linker metadata for the DLL's exported entry points) is the way DLLs get used. Dynamic loading is reserved typically for implementing "polymorphism" or "runtime configurability" in program behaviors (accessing add-ons or later-defined functionality, aka "plugins").</p>

<p>The Windows way of doing things can cause some confusion at times; the system uses the .LIB extension to refer to both normal static libraries (archives, like POSIX *.a files) and to the "export stub" libraries needed to bind an application to a DLL at link time. So, one should always look to see if a *.LIB file has a same-named *.DLL file; if not, chances are good that *.LIB file is a static library archive, and not export binding metadata for a DLL.</p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2014-04-19T12:12:29"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="23169909">
    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

            <div class="flex--item">
                <a href="/a/23169909" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f" data-se-share-sheet-license-name="CC BY-SA 3.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-3" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-3"><div class="s-popover--arrow"></div><div><label class="js-title fw-bold" for="share-sheet-input-se-share-sheet-3">Share a link to this answer</label> <span class="js-subtitle"></span></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-3" class="js-input s-input wmn3 sm:wmn-initial bc-black-200 bg-white fc-dark" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 3.0">CC BY-SA 3.0</a><div class="js-social-container d-none"></div></div></div>
            </div>


                    <div class="flex--item">
                        <a href="/posts/23169909/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

            <div class="flex--item">
                <button type="button" id="btnFollowPost-23169909" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-909pjhde">
                    Follow
                </button><div id="--stacks-s-tooltip-909pjhde" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
            </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info ">
    <div class="user-action-time">
        answered <span title="2014-04-19 12:12:29Z" class="relativetime">Apr 19, 2014 at 12:12</span>
    </div>
    <div class="user-gravatar32">
        <a href="/users/2833055/jogusto"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/?s=64&amp;d=identicon&amp;r=PG&amp;f=1" alt="JoGusto's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/2833055/jogusto">JoGusto</a><span class="d-none" itemprop="name">JoGusto</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">913</span><span title="8 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">8</span></span><span class="v-visible-sr">8 silver badges</span><span title="8 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">8</span></span><span class="v-visible-sr">8 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




            <span class="d-none" itemprop="commentCount"></span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-23169909" class="comments js-comments-container bt bc-black-075 mt12  dno" data-post-id="23169909" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

            </ul>
	    </div>

        <div id="comments-link-23169909" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>         
    </div>
    </div>
</div>

<div class="js-zone-container zone-container-main">
    <div id="dfp-smlb" class="everyonelovesstackoverflow everyoneloves__mid-second-leaderboard everyoneloves__leaderboard" style="min-height: auto; height: auto; display: none;" data-google-query-id="CPCJpb6EkPwCFXvQ_QUdSE4HTg"><div id="google_ads_iframe_/248424177/stackoverflow.com/smlb/question-pages_0__container__" style="border: 0pt none; width: 728px; height: 0px;"></div></div>
		<div class="js-report-ad-button-container " style="width: 728px"></div>
</div>
                                        
<a name="9688345"></a>
<div id="answer-9688345" class="answer js-answer" data-answerid="9688345" data-parentid="9688200" data-score="7" data-position-on-page="4" data-highest-scored="0" data-question-has-accepted-highest-score="0" itemprop="suggestedAnswer" itemscope="" itemtype="https://schema.org/Answer">
    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container d-flex jc-center fd-column ai-stretch gs4 fc-black-200" data-post-id="9688345">
        <button class="js-vote-up-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-hq6y6tyq">
            <svg aria-hidden="true" class="svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 25h32L18 9 2 25Z"></path></svg>
        </button><div id="--stacks-s-tooltip-hq6y6tyq" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title" itemprop="upvoteCount" data-value="7">
            7
        </div>
        <button class="js-vote-down-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-3z8v7pda">
            <svg aria-hidden="true" class="svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 11h32L18 27 2 11Z"></path></svg>
        </button><div id="--stacks-s-tooltip-3z8v7pda" class="s-popover s-popover__tooltip" role="tooltip">This answer is not useful<div class="s-popover--arrow"></div></div>


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" id="saves-btn-9688345" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" aria-pressed="false" data-post-id="9688345" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-1kqc7idj">
    <svg aria-hidden="true" class="fc-theme-primary-500 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26l4-2.66ZM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
</button><div id="--stacks-s-tooltip-1kqc7idj" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-700 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8v-8Z"></path></svg>
                </div>
            </div>

    
        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/9688345/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-wdttpo3p"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"></path></svg></a><div id="--stacks-s-tooltip-wdttpo3p" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>You are correct in that <strong>static files are copied to the application at link-time</strong>, and that <strong>shared files are just verified at link time and loaded at runtime</strong>.</p>
<p>The <code>dlopen</code> call is not only for shared objects, if the application wishes to do so at runtime on its behalf, otherwise the shared objects are loaded automatically when the application starts. DLLS and <code>.so</code> are the same thing. the <code>dlopen</code> exists to add even more fine-grained dynamic loading abilities for processes. You dont have to use <code>dlopen</code> yourself to open/use the DLLs, that happens too at application startup.</p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2012-03-13T16:46:06"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="9688345">
    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

            <div class="flex--item">
                <a href="/a/9688345" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f4.0%2f" data-se-share-sheet-license-name="CC BY-SA 4.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-4" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-4"><div class="s-popover--arrow"></div><div><label class="js-title fw-bold" for="share-sheet-input-se-share-sheet-4">Share a link to this answer</label> <span class="js-subtitle"></span></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-4" class="js-input s-input wmn3 sm:wmn-initial bc-black-200 bg-white fc-dark" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 4.0">CC BY-SA 4.0</a><div class="js-social-container d-none"></div></div></div>
            </div>


                    <div class="flex--item">
                        <a href="/posts/9688345/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

            <div class="flex--item">
                <button type="button" id="btnFollowPost-9688345" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-327dvu2z">
                    Follow
                </button><div id="--stacks-s-tooltip-327dvu2z" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
            </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>
            <div class="post-signature flex--item fl0">
<div class="user-info user-hover">
    <div class="user-action-time">
        <a href="/posts/9688345/revisions" title="show all edits to this post" class="js-gps-track" data-gps-track="post.click({ item: 4, priv: 0, post_type: 2 })">edited <span title="2021-11-03 17:38:53Z" class="relativetime">Nov 3, 2021 at 17:38</span></a>
    </div>
    <div class="user-gravatar32">
        <a href="/users/432903/prayagupa"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/584ab25408a84a589c0f7653a169499c?s=64&amp;d=identicon&amp;r=PG&amp;f=1" alt="prayagupa's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details">
        <a href="/users/432903/prayagupa">prayagupa</a>
        <div class="-flair">
            <span class="reputation-score" title="reputation score 29,514" dir="ltr">29.5k</span><span title="14 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">14</span></span><span class="v-visible-sr">14 gold badges</span><span title="150 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">150</span></span><span class="v-visible-sr">150 silver badges</span><span title="191 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">191</span></span><span class="v-visible-sr">191 bronze badges</span>
        </div>
    </div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info user-hover">
    <div class="user-action-time">
        answered <span title="2012-03-13 16:46:06Z" class="relativetime">Mar 13, 2012 at 16:46</span>
    </div>
    <div class="user-gravatar32">
        <a href="/users/405018/rapadura"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/88c946badb3bf2f930ea4314abb11641?s=64&amp;d=identicon&amp;r=PG" alt="rapadura's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/405018/rapadura">rapadura</a><span class="d-none" itemprop="name">rapadura</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">5,114</span><span title="7 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">7</span></span><span class="v-visible-sr">7 gold badges</span><span title="38 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">38</span></span><span class="v-visible-sr">38 silver badges</span><span title="57 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">57</span></span><span class="v-visible-sr">57 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




            <span class="d-none" itemprop="commentCount">3</span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-9688345" class="comments js-comments-container bt bc-black-075 mt12 " data-post-id="9688345" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

                        <li id="comment-12310397" class="comment js-comment " data-comment-id="12310397" data-comment-owner-id="1022889" data-comment-score="1">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">1</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">What would be one example of using dlopen() for more loading control? If the SO/DLL is auto-loaded at startup, does dlopen() close and re-open it with different permissions or restrictions, for example? Thank you.</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/1022889/cloud" title="18,393 reputation" class="comment-user owner">Cloud</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12310397_9688345" aria-label="Link to comment"><span title="2012-03-13 16:49:27Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 16:49</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-12310466" class="comment js-comment " data-comment-id="12310466" data-comment-owner-id="405018" data-comment-score="2">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">2</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">I believe the dlopen is for plugins or similar functionality. The permissions/restrictions should be the same as for the automatic loading, and anyway a dlopen will recursively load dependent libraries.</span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/405018/rapadura" title="5,114 reputation" class="comment-user">rapadura</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment12310466_9688345" aria-label="Link to comment"><span title="2012-03-13 16:51:41Z, License: CC BY-SA 3.0" class="relativetime-clean">Mar 13, 2012 at 16:51</span></a></span>
            </div>
        </div>
    </li>
    <li id="comment-94240169" class="comment js-comment " data-comment-id="94240169" data-comment-owner-id="841108" data-comment-score="1">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-edit-hide">
                    <span title="number of 'useful comment' votes received" class="cool">1</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">DLL and <code>.so</code> are <i>not exactly</i> the same thing. See <a href="https://stackoverflow.com/a/53691370/841108">this answer</a></span>
                
              <div class="d-inline-flex ai-center">
–&nbsp;<a href="/users/841108/basile-starynkevitch" title="1 reputation" class="comment-user">Basile Starynkevitch</a>
                </div>
                <span class="comment-date" dir="ltr"><a class="comment-link" href="#comment94240169_9688345" aria-label="Link to comment"><span title="2018-12-09 12:25:33Z, License: CC BY-SA 4.0" class="relativetime-clean">Dec 9, 2018 at 12:25</span></a></span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-9688345" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>         
    </div>
    </div>
</div>

                                        
<a name="70823134"></a>
<div id="answer-70823134" class="answer js-answer" data-answerid="70823134" data-parentid="9688200" data-score="-1" data-position-on-page="5" data-highest-scored="0" data-question-has-accepted-highest-score="0" itemprop="suggestedAnswer" itemscope="" itemtype="https://schema.org/Answer">
    <div class="post-layout">
        <div class="votecell post-layout--left">
            <div class="js-voting-container d-flex jc-center fd-column ai-stretch gs4 fc-black-200" data-post-id="70823134">
        <button class="js-vote-up-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Up vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-7a5b4zo3">
            <svg aria-hidden="true" class="svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 25h32L18 9 2 25Z"></path></svg>
        </button><div id="--stacks-s-tooltip-7a5b4zo3" class="s-popover s-popover__tooltip" role="tooltip">This answer is useful<div class="s-popover--arrow"></div></div>
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title" itemprop="upvoteCount" data-value="-1">
            -1
        </div>
        <button class="js-vote-down-btn flex--item s-btn s-btn__unset c-pointer " data-controller="s-tooltip" data-s-tooltip-placement="right" aria-pressed="false" aria-label="Down vote" data-selected-classes="fc-theme-primary" data-unselected-classes="" aria-describedby="--stacks-s-tooltip-0v626nh0">
            <svg aria-hidden="true" class="svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 11h32L18 27 2 11Z"></path></svg>
        </button><div id="--stacks-s-tooltip-0v626nh0" class="s-popover s-popover__tooltip" role="tooltip">This answer is not useful<div class="s-popover--arrow"></div></div>


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4" id="saves-btn-70823134" data-controller="s-tooltip" data-s-tooltip-placement="right" data-s-popover-placement="" aria-pressed="false" data-post-id="70823134" data-post-type-id="2" data-user-privilege-for-post-click="0" aria-controls="" data-s-popover-auto-show="false" aria-describedby="--stacks-s-tooltip-u5encit4">
    <svg aria-hidden="true" class="fc-theme-primary-500 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18" viewBox="0 0 18 18"><path d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18" viewBox="0 0 18 18"><path d="m9 10.6 4 2.66V3H5v10.26l4-2.66ZM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4-6 4Z"></path></svg>
</button><div id="--stacks-s-tooltip-u5encit4" class="s-popover s-popover__tooltip" role="tooltip">Save this answer.<div class="s-popover--arrow"></div></div>







            <div class="js-accepted-answer-indicator flex--item fc-green-700 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted…" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36"><path d="m6 14 8 8L30 6v8L14 30l-8-8v-8Z"></path></svg>
                </div>
            </div>

    
        <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/70823134/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" aria-label="Timeline" aria-describedby="--stacks-s-tooltip-psg30mtp"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18" viewBox="0 0 19 18"><path d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4h3L3 9Zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10V5Z"></path></svg></a><div id="--stacks-s-tooltip-psg30mtp" class="s-popover s-popover__tooltip" role="tooltip">Show activity on this post.<div class="s-popover--arrow"></div></div>

</div>

        </div>

        

<div class="answercell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
<p>I suspect some kind of misunderstanding here, but header files, at least of the .h variety used for compiling source code, are most definitely NOT checked during link time.</p>
<p>.h, and for that matter, .c/.cpp files, are only involved during the compilation phase, which includes preprocessing.  Once the object code has been created the header file is long gone well before the linker gets around to dealing with things.</p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2022-01-23T14:38:07"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="70823134">
    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

            <div class="flex--item">
                <a href="/a/70823134" rel="nofollow" itemprop="url" class="js-share-link js-gps-track" title="Short permalink to this answer" data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })" data-controller="se-share-sheet s-popover" data-se-share-sheet-title="Share a link to this answer" data-se-share-sheet-subtitle="" data-se-share-sheet-post-type="answer" data-se-share-sheet-social="facebook twitter devto" data-se-share-sheet-location="2" data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f4.0%2f" data-se-share-sheet-license-name="CC BY-SA 4.0" data-s-popover-placement="bottom-start" aria-controls="se-share-sheet-5" data-action=" s-popover#toggle se-share-sheet#preventNavigation s-popover:show->se-share-sheet#willShow s-popover:shown->se-share-sheet#didShow" aria-expanded="false">Share</a><div class="s-popover z-dropdown s-anchors s-anchors__default" style="width: unset; max-width: 28em;" id="se-share-sheet-5"><div class="s-popover--arrow"></div><div><label class="js-title fw-bold" for="share-sheet-input-se-share-sheet-5">Share a link to this answer</label> <span class="js-subtitle"></span></div><div class="my8"><input type="text" id="share-sheet-input-se-share-sheet-5" class="js-input s-input wmn3 sm:wmn-initial bc-black-200 bg-white fc-dark" readonly=""></div><div class="d-flex jc-space-between ai-center mbn4"><button class="js-copy-link-btn s-btn s-btn__link js-gps-track" data-gps-track="">Copy link</button><a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license" class="js-license s-block-link w-auto" target="_blank" title="The current license for this post: CC BY-SA 4.0">CC BY-SA 4.0</a><div class="js-social-container d-none"></div></div></div>
            </div>


                    <div class="flex--item">
                        <a href="/posts/70823134/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

            <div class="flex--item">
                <button type="button" id="btnFollowPost-70823134" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track" data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })" data-controller="s-tooltip " data-s-tooltip-placement="bottom" data-s-popover-placement="bottom" aria-controls="" aria-describedby="--stacks-s-tooltip-eq70lwox">
                    Follow
                </button><div id="--stacks-s-tooltip-eq70lwox" class="s-popover s-popover__tooltip" role="tooltip">Follow this answer to receive notifications<div class="s-popover--arrow"></div></div>
            </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info ">
    <div class="user-action-time">
        answered <span title="2022-01-23 14:38:07Z" class="relativetime">Jan 23 at 14:38</span>
    </div>
    <div class="user-gravatar32">
        <a href="/users/4705816/raymond-jennings"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/7221f4d854eaf1de9517520039aec5f2?s=64&amp;d=identicon&amp;r=PG" alt="Raymond Jennings's user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
        <a href="/users/4705816/raymond-jennings">Raymond Jennings</a><span class="d-none" itemprop="name">Raymond Jennings</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">109</span><span title="2 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">2</span></span><span class="v-visible-sr">2 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




            <span class="d-none" itemprop="commentCount">0</span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-70823134" class="comments js-comments-container bt bc-black-075 mt12  dno" data-post-id="70823134" data-min-length="15">
            <ul class="comments-list js-comments-list" data-remaining-comments-count="0" data-canpost="false" data-cansee="true" data-comments-unavailable="false" data-addlink-disabled="true">

            </ul>
	    </div>

        <div id="comments-link-70823134" data-rep="50" data-anon="true">
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”." href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href="#" onclick="" role="button"></a>
        </div>         
    </div>
    </div>
</div>


                        <a name="new-answer"></a>
                            <form id="post-form" action="/questions/9688200/answer/submit" method="post" class="js-add-answer-component post-form">
                                <input type="hidden" id="post-id" value="9688200">
                                <input type="hidden" id="qualityBanWarningShown" name="qualityBanWarningShown" value="false">
                                <input type="hidden" name="referrer" value="https://www.bing.com/">
                                <h2 class="space" id="your-answer-header">
                                    Your Answer
                                </h2>
                                    

    <script>
        StackExchange.ifUsing("editor", function () {
            StackExchange.using("externalEditor", function () {
                StackExchange.using("snippets", function () {
                    StackExchange.snippets.init();
                });
            });
        }, "code-snippets");
    </script>


<script>
    StackExchange.ready(function() {
        var channelOptions = {
            tags: "".split(" "),
            id: "1"
        };
        initTagRenderer("".split(" "), "".split(" "), channelOptions);

        StackExchange.using("externalEditor", function() {
            // Have to fire editor after snippets, if snippets enabled
            if (StackExchange.settings.snippets.snippetsEnabled) {
                StackExchange.using("snippets", function() {
                    createEditor();
                });
            }
            else {
                createEditor();
            }
        });

        function createEditor() {
            StackExchange.prepareEditor({
                useStacksEditor: false,
                heartbeatType: 'answer',
                autoActivateHeartbeat: false,
                convertImagesToLinks: true,
                noModals: true,
                showLowRepImageUploadWarning: true,
                reputationToPostImages: 10,
                bindNavPrevention: true,
                postfix: "",
                imageUploader: {
                    brandingHtml: "Powered by \u003ca href=\"https://imgur.com/\"\u003e\u003csvg class=\"svg-icon\" width=\"50\" height=\"18\" viewBox=\"0 0 50 18\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\"\u003e\u003ctitle\u003eImgur Logo\u003c/title\u003e\u003cpath d=\"M46.1709 9.17788C46.1709 8.26454 46.2665 7.94324 47.1084 7.58816C47.4091 7.46349 47.7169 7.36433 48.0099 7.26993C48.9099 6.97997 49.672 6.73443 49.672 5.93063C49.672 5.22043 48.9832 4.61182 48.1414 4.61182C47.4335 4.61182 46.7256 4.91628 46.0943 5.50789C45.7307 4.9328 45.2525 4.66231 44.6595 4.66231C43.6264 4.66231 43.1481 5.28821 43.1481 6.59048V11.9512C43.1481 13.2535 43.6264 13.8962 44.6595 13.8962C45.6924 13.8962 46.1709 13.2535 46.1709 11.9512V9.17788Z\"/\u003e\u003cpath d=\"M32.492 10.1419C32.492 12.6954 34.1182 14.0484 37.0451 14.0484C39.9723 14.0484 41.5985 12.6954 41.5985 10.1419V6.59049C41.5985 5.28821 41.1394 4.66232 40.1061 4.66232C39.0732 4.66232 38.5948 5.28821 38.5948 6.59049V9.60062C38.5948 10.8521 38.2696 11.5455 37.0451 11.5455C35.8209 11.5455 35.4954 10.8521 35.4954 9.60062V6.59049C35.4954 5.28821 35.0173 4.66232 34.0034 4.66232C32.9703 4.66232 32.492 5.28821 32.492 6.59049V10.1419Z\" /\u003e\u003cpath fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M25.6622 17.6335C27.8049 17.6335 29.3739 16.9402 30.2537 15.6379C30.8468 14.7755 30.9615 13.5579 30.9615 11.9512V6.59049C30.9615 5.28821 30.4833 4.66231 29.4502 4.66231C28.9913 4.66231 28.4555 4.94978 28.1109 5.50789C27.499 4.86533 26.7335 4.56087 25.7005 4.56087C23.1369 4.56087 21.0134 6.57349 21.0134 9.27932C21.0134 11.9852 23.003 13.913 25.3754 13.913C26.5612 13.913 27.4607 13.4902 28.1109 12.6616C28.1109 12.7229 28.1161 12.7799 28.121 12.8346C28.1256 12.8854 28.1301 12.9342 28.1301 12.983C28.1301 14.4373 27.2502 15.2321 25.777 15.2321C24.8349 15.2321 24.1352 14.9821 23.5661 14.7787C23.176 14.6393 22.8472 14.5218 22.5437 14.5218C21.7977 14.5218 21.2429 15.0123 21.2429 15.6887C21.2429 16.7375 22.9072 17.6335 25.6622 17.6335ZM24.1317 9.27932C24.1317 7.94324 24.9928 7.09766 26.1024 7.09766C27.2119 7.09766 28.0918 7.94324 28.0918 9.27932C28.0918 10.6321 27.2311 11.5116 26.1024 11.5116C24.9737 11.5116 24.1317 10.6491 24.1317 9.27932Z\"/\u003e\u003cpath d=\"M16.8045 11.9512C16.8045 13.2535 17.2637 13.8962 18.2965 13.8962C19.3298 13.8962 19.8079 13.2535 19.8079 11.9512V8.12928C19.8079 5.82936 18.4879 4.62866 16.4027 4.62866C15.1594 4.62866 14.279 4.98375 13.3609 5.88013C12.653 5.05154 11.6581 4.62866 10.3573 4.62866C9.34336 4.62866 8.57809 4.89931 7.9466 5.5079C7.58314 4.9328 7.10506 4.66232 6.51203 4.66232C5.47873 4.66232 5.00066 5.28821 5.00066 6.59049V11.9512C5.00066 13.2535 5.47873 13.8962 6.51203 13.8962C7.54479 13.8962 8.0232 13.2535 8.0232 11.9512V8.90741C8.0232 7.58817 8.44431 6.91179 9.53458 6.91179C10.5104 6.91179 10.893 7.58817 10.893 8.94108V11.9512C10.893 13.2535 11.3711 13.8962 12.4044 13.8962C13.4375 13.8962 13.9157 13.2535 13.9157 11.9512V8.90741C13.9157 7.58817 14.3365 6.91179 15.4269 6.91179C16.4027 6.91179 16.8045 7.58817 16.8045 8.94108V11.9512Z\"/\u003e\u003cpath d=\"M3.31675 6.59049C3.31675 5.28821 2.83866 4.66232 1.82471 4.66232C0.791758 4.66232 0.313354 5.28821 0.313354 6.59049V11.9512C0.313354 13.2535 0.791758 13.8962 1.82471 13.8962C2.85798 13.8962 3.31675 13.2535 3.31675 11.9512V6.59049Z\" /\u003e\u003cpath d=\"M1.87209 0.400291C0.843612 0.400291 0 1.1159 0 1.98861C0 2.87869 0.822846 3.57676 1.87209 3.57676C2.90056 3.57676 3.7234 2.87869 3.7234 1.98861C3.7234 1.1159 2.90056 0.400291 1.87209 0.400291Z\" fill=\"#1BB76E\"/\u003e\u003c/svg\u003e\u003c/a\u003e",
                    contentPolicyHtml: "User contributions licensed under \u003ca href=\"https://stackoverflow.com/help/licensing\"\u003eCC BY-SA\u003c/a\u003e \u003ca href=\"https://stackoverflow.com/legal/content-policy\"\u003e(content policy)\u003c/a\u003e",
                    allowUrls: true
                },
                onDemand: true,
                discardSelector: ".discard-answer",
                enableTables: true,
                isStacksEditorPreviewEnabled: false
                ,immediatelyShowMarkdownHelp:true,enableTables:true,enableSnippets:true
            });
                    }
    });
</script>
<div id="post-editor" class="post-editor js-post-editor">


        <div class="ps-relative">
            <div class="wmd-container mb8">
                <div id="wmd-button-bar" class="wmd-button-bar btr-sm"><ul id="wmd-button-row" class="wmd-button-row"><li id="wmd-bold-button" class="wmd-button" style="left: 0px;"><span style="background-position: 0px -20px;"></span></li><li id="wmd-italic-button" class="wmd-button" style="left: 25px;"><span style="background-position: -20px -20px;"></span></li><li id="wmd-spacer1" class="wmd-spacer" style="left: 50px;"><span style="background-position: -40px -20px;"></span></li><li id="wmd-link-button" class="wmd-button" style="left: 75px;"><span style="background-position: -40px -20px;"></span></li><li id="wmd-quote-button" class="wmd-button" style="left: 100px;"><span style="background-position: -60px -20px;"></span></li><li id="wmd-code-button" class="wmd-button" style="left: 125px;"><span style="background-position: -80px -20px;"></span></li><li id="wmd-image-button" class="wmd-button" style="left: 150px;"><span style="background-position: -100px -20px;"></span></li><li id="wmd-spacer2" class="wmd-spacer" style="left: 175px;"><span style="background-position: -120px -20px;"></span></li><li id="wmd-olist-button" class="wmd-button" style="left: 200px;"><span style="background-position: -120px -20px;"></span></li><li id="wmd-ulist-button" class="wmd-button" style="left: 225px;"><span style="background-position: -140px -20px;"></span></li><li id="wmd-heading-button" class="wmd-button" style="left: 250px;"><span style="background-position: -160px -20px;"></span></li><li id="wmd-hr-button" class="wmd-button" style="left: 275px;"><span style="background-position: -180px -20px;"></span></li><li id="wmd-spacer3" class="wmd-spacer" style="left: 300px;"><span style="background-position: -200px -20px;"></span></li><li id="wmd-undo-button" class="wmd-button" style="left: 325px;"><span style="background-position: -200px -20px;"></span></li><li id="wmd-redo-button" class="wmd-button" style="left: 350px;"><span style="background-position: -220px -20px;"></span></li><li class="wmd-spacer wmd-spacer-max"></li></ul></div>
                <div class="js-stacks-validation">
                    <div class="ps-relative">
                        <textarea id="wmd-input" name="post-text" class="wmd-input s-input bar0 js-post-body-field" data-editor-type="wmd" data-post-type-id="2" cols="92" rows="15" aria-labelledby="your-answer-header" tabindex="101" data-min-length=""></textarea>
                    </div>
                    <div class="s-input-message mt4 d-none js-stacks-validation-message"></div>
                </div>
            </div>
        </div>

    <aside class="d-flex ai-start jc-space-between js-answer-help s-notice s-notice__warning pb0 pr4 pt4 mb8 d-none" role="status" aria-hidden="true">
    <div class="flex--item pt8">
        <p>Thanks for contributing an answer to Stack Overflow!</p><ul><li>Please be sure to <em>answer the question</em>. Provide details and share your research!</li></ul><p>But <em>avoid</em> …</p><ul><li>Asking for help, clarification, or responding to other answers.</li><li>Making statements based on opinion; back them up with references or personal experience.</li></ul><p>To learn more, see our <a href="/help/how-to-answer">tips on writing great answers</a>.</p>
    </div>
    <button class="flex--item js-answer-help-close-btn s-btn s-btn__muted fc-dark">
        <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9 15 4.41Z"></path></svg>
    </button>
</aside>



    <div>
        <div id="draft-saved" class="fc-success h24" style="display:none;">Draft saved</div>
        <div id="draft-discarded" class="fc-error h24" style="display:none;">Draft discarded</div>
    </div>


            <div id="wmd-preview" class="s-prose mb16 wmd-preview js-wmd-preview"></div>
            <div></div>

        <div class="edit-block">
            <input id="fkey" name="fkey" type="hidden" value="57626a78caee3eb0bd6fd5e0940aee94740c698e816bbd2d12d050fc41b3a36d">
            <input id="author" name="author" type="text">
        </div>

</div>


                                <div class="ps-relative">
                                                <div class="form-item new-post-login p0 my16">
                <div class="d-flex gs16 md:fd-column new-login-form">
                    <div class="d-flex fd-column w50 md:w-auto gsy gs8 jc-space-between new-login-left">
                        <h3 class="flex--item fs-title">Sign up or <a id="login-link" href="/users/login?ssrc=question_page&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f9688200%2fdifference-between-shared-objects-so-static-libraries-a-and-dlls-so%23new-answer">log in</a></h3>
                        <script>
                            StackExchange.ready(function () {
                                StackExchange.helpers.onClickDraftSave('#login-link');
                            });
                        </script>
                        <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon google-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Google&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconGoogle" width="18" height="18" viewBox="0 0 18 18"><path d="M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18Z" fill="#4285F4"></path><path d="M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17Z" fill="#34A853"></path><path d="M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18l2.67-2.07Z" fill="#FBBC05"></path><path d="M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.77 4.77 0 0 1 4.48-3.3Z" fill="#EA4335"></path></svg> Sign up using Google
                        </div>
                        <div class="flex--item s-btn s-btn__muted s-btn__icon facebook-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Facebook&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="svg-icon iconFacebook" width="18" height="18" viewBox="0 0 18 18"><path d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3Zm6.55 16v-6.2H7.46V8.4h2.09V6.61c0-2.07 1.26-3.2 3.1-3.2.88 0 1.64.07 1.87.1v2.16h-1.29c-1 0-1.19.48-1.19 1.18V8.4h2.39l-.31 2.42h-2.08V17h-2.5Z" fill="#4167B2"></path></svg> Sign up using Facebook
                        </div>
                        <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon stackexchange-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconLogoGlyphXSm" width="18" height="18" viewBox="0 0 18 18"><path d="M14 16v-5h2v7H2v-7h2v5h10Z" fill="#BCBBBB"></path><path d="m12.09.72-1.21.9 4.5 6.07 1.22-.9L12.09.71ZM5 15h8v-2H5v2Zm9.15-5.87L8.35 4.3l.96-1.16 5.8 4.83-.96 1.16Zm-7.7-1.47 6.85 3.19.63-1.37-6.85-3.2-.63 1.38Zm6.53 5L5.4 11.39l.38-1.67 7.42 1.48-.22 1.46Z" fill="#F48024"></path></svg> Sign up using Email and Password
                        </div>
                    </div>
                    <input type="hidden" name="use-facebook" class="use-facebook" value="false">
                    <input type="hidden" name="use-google" class="use-google" value="false">
                    <button type="button" class="d-none js-submit-openid">Submit</button>
                    <div class="d-flex gsy gs8 fd-column w50 md:w-auto new-login-right form-item p0">
                                <h3 class="flex--item fs-title">Post as a guest</h3>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="d-flex ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="">
                    </div>
                </div>
            </div>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <div class="flex--item">
                        <div class="d-flex gs2 gsy fd-column">
                            <label class="flex--item s-label" for="m-address">Email</label>
                            <p class="flex--item s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="d-flex ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="">
                    </div>
                </div>
            </div>

                    </div>
                </div>
            </div>
            <script>
                StackExchange.ready(
                    function () {
                        StackExchange.openid.initPostLogin('.new-post-login', 'https%3a%2f%2fstackoverflow.com%2fquestions%2f9688200%2fdifference-between-shared-objects-so-static-libraries-a-and-dlls-so%23new-answer', 'question_page');
                    }
                );
            </script>
            <noscript>
                        <h3 class="flex--item fs-title">Post as a guest</h3>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="d-flex ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="" />
                    </div>
                </div>
            </div>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <div class="flex--item">
                        <div class="d-flex gs2 gsy fd-column">
                            <label class="flex--item s-label" for="m-address">Email</label>
                            <p class="flex--item s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="d-flex ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="" />
                    </div>
                </div>
            </div>

            </noscript>

                                </div>

                                    <div class="form-submit clear-both d-flex gsx gs4">
                                        <button id="submit-button" class="flex--item s-btn s-btn__primary s-btn__icon" type="submit" tabindex="120" autocomplete="off">
Post Your Answer                                        </button>
                                        <button class="flex--item s-btn s-btn__danger discard-answer dno">
                                            Discard
                                        </button>
                                            <p class="privacy-policy-agreement">
                                                By clicking “Post Your Answer”, you agree to our <a href="https://stackoverflow.com/legal/terms-of-service/public" name="tos" target="_blank" class="-link">terms of service</a>, <a href="https://stackoverflow.com/legal/privacy-policy" name="privacy" target="_blank" class="-link">privacy policy</a> and <a href="https://stackoverflow.com/legal/cookie-policy" name="cookie" target="_blank" class="-link">cookie policy</a><input type="hidden" name="legalLinksShown" value="1">
                                            </p>
                                    </div>
                                    <div class="js-general-error general-error clear-both d-none" aria-live="polite"></div>
                            </form>


                            <h2 class="bottom-notice" data-loc="1">
                                <div>
Not the answer you're looking for? Browse other questions tagged <ul class="ml0 list-ls-none js-post-tag-list-wrapper d-inline"><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/c%2b%2b" class="post-tag" title="show questions tagged 'c++'" aria-label="show questions tagged 'c++'" rel="tag" aria-labelledby="c++-container">c++</a></li><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/c" class="post-tag" title="show questions tagged 'c'" aria-label="show questions tagged 'c'" rel="tag" aria-labelledby="c-container">c</a></li><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/linux" class="post-tag" title="show questions tagged 'linux'" aria-label="show questions tagged 'linux'" rel="tag" aria-labelledby="linux-container">linux</a></li><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/dll" class="post-tag" title="show questions tagged 'dll'" aria-label="show questions tagged 'dll'" rel="tag" aria-labelledby="dll-container">dll</a></li><li class="d-inline mr4 js-post-tag-list-item"><a href="/questions/tagged/linker" class="post-tag" title="show questions tagged 'linker'" aria-label="show questions tagged 'linker'" rel="tag" aria-labelledby="linker-container">linker</a></li></ul> or <a href="/questions/ask">ask your own question</a>.                                </div>
                            </h2>
                </div>
            </div>

                
<div id="sidebar" class="show-votes" role="complementary" aria-label="sidebar">
        

    
<div class="s-sidebarwidget s-sidebarwidget__yellow s-anchors s-anchors__grayscale mb16" data-tracker="cb=1">
    <ul class="d-block p0 m0">
                    <li class="s-sidebarwidget--header s-sidebarwidget__small-bold-text d-flex fc-black-600 d:fc-black-900 bb bbw1">
                        The Overflow Blog
                    </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0ZM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88Z"></path></svg>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://stackoverflow.blog/2022/12/22/the-complete-guide-to-protecting-your-apis-with-oauth2/?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2022/12/22/the-complete-guide-to-protecting-your-apis-with-oauth2/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 0 })">The complete guide to protecting your APIs with OAuth2 (part 1)</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14" viewBox="0 0 14 14"><path d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0ZM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88Z"></path></svg>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://stackoverflow.blog/2022/12/23/the-three-top-paying-tech-roles-in-2022-and-the-skills-you-need-to-land-them/?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2022/12/23/the-three-top-paying-tech-roles-in-2022-and-the-skills-you-need-to-land-them/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 1 })">The three top-paying tech roles in 2022 and the skills you need to land them</a>
                    <div class="fc-light fs-italic">sponsored post</div>
            </div>
        </li>
                    <li class="s-sidebarwidget--header s-sidebarwidget__small-bold-text d-flex fc-black-600 d:fc-black-900 bb bbw1">
                        Featured on Meta
                    </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackexchange.com/questions/384406/navigation-and-ui-research-starting-soon?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/384406/navigation-and-ui-research-starting-soon&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 2 })">Navigation and UI research starting soon</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackoverflow.com/questions/421619/2022-community-moderator-election-results-now-with-two-more-mods?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackoverflow.com/questions/421619/2022-community-moderator-election-results-now-with-two-more-mods&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 6, position: 3 })">2022 Community Moderator Election Results - now with two more mods!</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackoverflow.com/questions/421831/temporary-policy-chatgpt-is-banned?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackoverflow.com/questions/421831/temporary-policy-chatgpt-is-banned&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 6, position: 4 })">Temporary policy: ChatGPT is banned</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackoverflowmeta" title="Meta Stack Overflow"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackoverflow.com/questions/422180/im-standing-down-as-a-moderator?cb=1" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackoverflow.com/questions/422180/im-standing-down-as-a-moderator&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 6, position: 5 })">I'm standing down as a moderator</a>
            </div>
        </li>
    </ul>
</div>


<div class="js-zone-container zone-container-sidebar">
    <div id="dfp-tsb" class="everyonelovesstackoverflow everyoneloves__top-sidebar" data-dfp-zone="true" style="min-height: auto; height: auto;" data-google-query-id="CK_WpL6EkPwCFcLm_QUd-rMBOw"><div id="google_ads_iframe_/248424177/stackoverflow.com/sb/question-pages_0__container__" style="border: 0pt none; display: inline-block; width: 300px; height: 250px;"><iframe frameborder="0" src="https://6069a9ccde7913e3c1d8e794842d62f0.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html" id="google_ads_iframe_/248424177/stackoverflow.com/sb/question-pages_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="300" height="250" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" role="region" aria-label="Advertisement" tabindex="0" data-google-container-id="2" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div></div>
		<div class="js-report-ad-button-container " style="width: 300px; height: 24px;"><button data-google-event-data="{&quot;serviceName&quot;:&quot;publisher_ads&quot;,&quot;slot&quot;:{},&quot;isEmpty&quot;:false,&quot;slotContentChanged&quot;:true,&quot;size&quot;:[300,250],&quot;advertiserId&quot;:4933108035,&quot;campaignId&quot;:2945342793,&quot;creativeId&quot;:138415077675,&quot;creativeTemplateId&quot;:null,&quot;labelIds&quot;:null,&quot;lineItemId&quot;:5847406694,&quot;sourceAgnosticCreativeId&quot;:138415077675,&quot;sourceAgnosticLineItemId&quot;:5847406694,&quot;isBackfill&quot;:false,&quot;yieldGroupIds&quot;:null,&quot;companyIds&quot;:null}" data-modal-url="/ads/report-ad" data-ad-unit="dfp-tsb" class="js-report-ad s-btn s-btn__link fs-fine mt2 float-right">Report this ad</button></div>
</div>
<div class="js-zone-container zone-container-sidebar">
    <div id="dfp-msb" class="everyonelovesstackoverflow everyoneloves__mid-sidebar" data-dfp-zone="true" style="min-height: auto; height: auto; display: none;" data-google-query-id="CNuDpb6EkPwCFY3M_QUdLKMPZw"><div id="google_ads_iframe_/248424177/stackoverflow.com/msb/question-pages_0__container__" style="border: 0pt none; width: 300px; height: 0px;"></div></div>
		<div class="js-report-ad-button-container " style="width: 300px"></div>
</div>
<div id="hireme"></div>        <div class="module sidebar-linked">
	<h4 id="h-linked">Linked</h4>
	<div class="linked" data-tracker="lq=1">
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 25236964, position: 0 })">
				<a href="https://stackoverflow.com/q/25236964?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes  default">3</div>
				</a>
				<a href="https://stackoverflow.com/questions/25236964/actual-purpose-of-shared-object?noredirect=1&amp;lq=1" class="question-hyperlink">Actual purpose of Shared object</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 25896207, position: 1 })">
				<a href="https://stackoverflow.com/q/25896207?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes answered-accepted default">36</div>
				</a>
				<a href="https://stackoverflow.com/questions/25896207/difference-between-code-object-and-executable-file?noredirect=1&amp;lq=1" class="question-hyperlink">Difference between code object and executable file</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 6181078, position: 2 })">
				<a href="https://stackoverflow.com/q/6181078?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes answered-accepted default">29</div>
				</a>
				<a href="https://stackoverflow.com/questions/6181078/why-are-static-and-dynamic-linkable-libraries-different?noredirect=1&amp;lq=1" class="question-hyperlink">Why are static and dynamic linkable libraries different?</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 53691295, position: 3 })">
				<a href="https://stackoverflow.com/q/53691295?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes answered-accepted default">10</div>
				</a>
				<a href="https://stackoverflow.com/questions/53691295/equivalent-of-import-libraries-in-linux?noredirect=1&amp;lq=1" class="question-hyperlink">Equivalent of import libraries in Linux</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 19633091, position: 4 })">
				<a href="https://stackoverflow.com/q/19633091?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes answered-accepted default">12</div>
				</a>
				<a href="https://stackoverflow.com/questions/19633091/difference-between-so-file-and-a-file?noredirect=1&amp;lq=1" class="question-hyperlink">Difference between .so file and .a file?</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 42017681, position: 5 })">
				<a href="https://stackoverflow.com/q/42017681?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes  default">12</div>
				</a>
				<a href="https://stackoverflow.com/questions/42017681/do-shared-libraries-so-files-need-to-present-or-specified-at-link-time?noredirect=1&amp;lq=1" class="question-hyperlink">Do shared libraries (.so) files need to present (or specified) at link time?</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 13295628, position: 6 })">
				<a href="https://stackoverflow.com/q/13295628?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes  default">5</div>
				</a>
				<a href="https://stackoverflow.com/questions/13295628/difference-between-a-shared-object-and-a-dll?noredirect=1&amp;lq=1" class="question-hyperlink">Difference between a shared object and a dll</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 67671247, position: 7 })">
				<a href="https://stackoverflow.com/q/67671247?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes  default">5</div>
				</a>
				<a href="https://stackoverflow.com/questions/67671247/clion-c-executable-vs-c-library?noredirect=1&amp;lq=1" class="question-hyperlink">Clion c++ executable vs C++ library</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 39483519, position: 8 })">
				<a href="https://stackoverflow.com/q/39483519?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes answered-accepted default">1</div>
				</a>
				<a href="https://stackoverflow.com/questions/39483519/c-c-hide-c-or-c-function-code-from-other-people?noredirect=1&amp;lq=1" class="question-hyperlink">C/C++ - Hide C or C++ function code from other people</a>
			</div>
            <div class="spacer js-gps-track" data-gps-track="linkedquestion.click({ source_post_id: 9688200, target_question_id: 22795558, position: 9 })">
				<a href="https://stackoverflow.com/q/22795558?lq=1" title="Question score (upvotes - downvotes)">
					<div class="answer-votes  default">2</div>
				</a>
				<a href="https://stackoverflow.com/questions/22795558/why-including-an-h-file-with-external-vars-and-funcs-results-in-undefined-refere?noredirect=1&amp;lq=1" class="question-hyperlink">Why including an h file with external vars and funcs results in undefined references</a>
			</div>
		    <div class="spacer more ml32 pl16 pt8">
                <a href="https://stackoverflow.com/questions/linked/9688200?lq=1">See more linked questions</a>
            </div>
	</div>
</div>


    
        <div class="module sidebar-related">
            <h4 id="h-related">Related</h4>
            <div class="related js-gps-related-questions" data-tracker="rq=1">
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/21593?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes extra-large">2954</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/21593/what-is-the-difference-between-include-filename-and-include-filename?rq=1" class="question-hyperlink">What is the difference between #include &lt;filename&gt; and #include "filename"?</a>
                    </div>
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/24853?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted extra-large">1111</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/24853/what-is-the-difference-between-i-and-i?rq=1" class="question-hyperlink">What is the difference between ++i and i++?</a>
                    </div>
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/57483?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes extra-large">3793</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/57483/what-are-the-differences-between-a-pointer-variable-and-a-reference-variable?rq=1" class="question-hyperlink">What are the differences between a pointer variable and a reference variable?</a>
                    </div>
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/172587?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted extra-large">1104</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/172587/what-is-the-difference-between-g-and-gcc?rq=1" class="question-hyperlink">What is the difference between g++ and gcc?</a>
                    </div>
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/1143262?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted extra-large">1706</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/1143262/what-is-the-difference-between-const-int-const-int-const-and-int-const?rq=1" class="question-hyperlink">What is the difference between const int*, const int * const, and int const *?</a>
                    </div>
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/1538420?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted large">907</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/1538420/difference-between-malloc-and-calloc?rq=1" class="question-hyperlink">Difference between malloc and calloc?</a>
                    </div>
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/1711631?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted extra-large">3275</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/1711631/improve-insert-per-second-performance-of-sqlite?rq=1" class="question-hyperlink">Improve INSERT-per-second performance of SQLite</a>
                    </div>
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/1993390?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted large">479</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/1993390/static-linking-vs-dynamic-linking?rq=1" class="question-hyperlink">Static linking vs dynamic linking</a>
                    </div>
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/2649334?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted large">652</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/2649334/difference-between-static-and-shared-libraries?rq=1" class="question-hyperlink">Difference between static and shared libraries?</a>
                    </div>
                    <div class="spacer">
                        <a href="https://stackoverflow.com/q/10747810?rq=1" title="Question score (upvotes - downvotes)">
                            <div class="answer-votes answered-accepted extra-large">1176</div>
                        </a>
                        <a href="https://stackoverflow.com/questions/10747810/what-is-the-difference-between-typedef-and-using-in-c11?rq=1" class="question-hyperlink">What is the difference between 'typedef' and 'using' in C++11?</a>
                    </div>
            </div>
        </div>



    <div id="hot-network-questions" class="module tex2jax_ignore">
    <h4>
        <a href="https://stackexchange.com/questions?tab=hot" class="js-gps-track s-link s-link__inherit" data-gps-track="posts_hot_network.click({ item_type:1, location:11 })">
            Hot Network Questions
        </a>
    </h4>
    <ul>
            <li>
                <div class="favicon favicon-mathoverflow" title="MathOverflow"></div><a href="https://mathoverflow.net/questions/437086/fixed-point-theorem-for-the-uncountable-power-of-an-interval" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:504 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Fixed point theorem for the uncountable power of an interval
                </a>

            </li>
            <li>
                <div class="favicon favicon-mathematica" title="Mathematica Stack Exchange"></div><a href="https://mathematica.stackexchange.com/questions/277684/why-is-mathematica-giving-such-an-incorrect-answer-for-these-integrals-huge-err" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:387 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why is Mathematica Giving Such an Incorrect Answer for These Integrals? Huge Error Estimate
                </a>

            </li>
            <li>
                <div class="favicon favicon-judaism" title="Mi Yodeya"></div><a href="https://judaism.stackexchange.com/questions/132308/ber-43-33-yosef-seats-the-brothers-in-birth-order-this-could-have-revealed" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:248 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Ber. 43 (33). Yosef seats the brothers in birth order. This could have revealed his identity prematurely?
                </a>

            </li>
            <li>
                <div class="favicon favicon-codegolf" title="Code Golf Stack Exchange"></div><a href="https://codegolf.stackexchange.com/questions/255850/8086-segment-address-to-linear" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:200 }); posts_hot_network.click({ item_type:2, location:11 })">
                    8086 Segment Address to Linear
                </a>

            </li>
            <li>
                <div class="favicon favicon-workplace" title="The Workplace Stack Exchange"></div><a href="https://workplace.stackexchange.com/questions/189188/when-to-reject-job-offer-when-i-have-another-offer-in-hand" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:423 }); posts_hot_network.click({ item_type:2, location:11 })">
                    When to reject job offer when I have another offer in hand?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-law" title="Law Stack Exchange"></div><a href="https://law.stackexchange.com/questions/87472/can-one-enforce-a-patent-while-it-is-only-pending-approval" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:617 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Can one enforce a patent while it is only "pending approval"?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-scifi" title="Science Fiction &amp; Fantasy Stack Exchange"></div><a href="https://scifi.stackexchange.com/questions/270506/husband-and-wife-contemplate-what-if-short-story-from-the-late-60s-or-early" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:186 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Husband and wife contemplate "What If" - Short story from the late 60's or early 70's
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-or" title="Operations Research Stack Exchange"></div><a href="https://or.stackexchange.com/questions/9623/adding-linear-penalties-for-multiple-assignments" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:700 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Adding linear penalties for multiple assignments
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-politics" title="Politics Stack Exchange"></div><a href="https://politics.stackexchange.com/questions/77245/what-does-a-lobbyist-offer-a-politician" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:475 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What does a lobbyist offer a politician?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-aviation" title="Aviation Stack Exchange"></div><a href="https://aviation.stackexchange.com/questions/96550/why-dont-airliner-vertical-tails-extend-to-the-very-aft-of-the-fuselage" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:528 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why don't airliner vertical tails extend to the very aft of the fuselage?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-money" title="Personal Finance &amp; Money Stack Exchange"></div><a href="https://money.stackexchange.com/questions/154296/prepaying-tax-vs-estimated-tax" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:93 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Prepaying tax vs. estimated tax
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-money" title="Personal Finance &amp; Money Stack Exchange"></div><a href="https://money.stackexchange.com/questions/154253/why-are-wire-transfers-not-reversible-by-the-bank" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:93 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why are wire transfers not reversible by the bank?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-stats" title="Cross Validated"></div><a href="https://stats.stackexchange.com/questions/599859/what-does-it-mean-by-maximum-likelihood-estimation-mle-problem-is-unbounded" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:65 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What does it mean by "maximum likelihood estimation (MLE) problem is unbounded"?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-unix" title="Unix &amp; Linux Stack Exchange"></div><a href="https://unix.stackexchange.com/questions/729344/why-cant-i-do-two-greps-after-a-tail" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:106 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why can't I do two greps after a tail?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-scifi" title="Science Fiction &amp; Fantasy Stack Exchange"></div><a href="https://scifi.stackexchange.com/questions/270501/is-this-gif-from-a-movie" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:186 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Is this gif from a movie?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-rpg" title="Role-playing Games Stack Exchange"></div><a href="https://rpg.stackexchange.com/questions/203565/dm-is-taking-too-much-time-in-my-opinion-on-side-missions-should-i-leave" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:122 }); posts_hot_network.click({ item_type:2, location:11 })">
                    DM is taking too much time in my opinion on side missions - should I leave?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-worldbuilding" title="Worldbuilding Stack Exchange"></div><a href="https://worldbuilding.stackexchange.com/questions/239765/why-would-a-molten-alloy-need-to-be-jettisoned-into-low-to-medium-orbit-to-cool" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:579 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why would a molten alloy need to be jettisoned into low-to-medium orbit to cool as part of the manufacturing process?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-academia" title="Academia Stack Exchange"></div><a href="https://academia.stackexchange.com/questions/191884/is-it-possible-to-have-the-contract-starting-date-before-actually-starting-to-wo" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:415 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Is it possible to have the contract starting date before actually starting to work?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-unix" title="Unix &amp; Linux Stack Exchange"></div><a href="https://unix.stackexchange.com/questions/729274/how-does-the-kernel-know-its-resuming-from-hibernation-not-booting" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:106 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How does the kernel know it's resuming from hibernation, not booting?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-physics" title="Physics Stack Exchange"></div><a href="https://physics.stackexchange.com/questions/742157/what-would-a-standing-wave-of-light-look-like" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:151 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What would a standing wave of light look like?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-biology" title="Biology Stack Exchange"></div><a href="https://biology.stackexchange.com/questions/111116/are-antibodies-and-immunoglobulins-really-the-same-things" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:375 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Are "antibodies" and "immunoglobulins" really the same things?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-chess" title="Chess Stack Exchange"></div><a href="https://chess.stackexchange.com/questions/41188/why-is-this-position-6-2-without-a-big-material-difference" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:435 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why is this position -6.2 without a big material difference?
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-tex" title="TeX - LaTeX Stack Exchange"></div><a href="https://tex.stackexchange.com/questions/669325/how-to-give-an-elliptical-border-a-braided-effect" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:85 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How to Give an Elliptical Border a Braided Effect
                </a>

            </li>
            <li class="js-hidden" style="">
                <div class="favicon favicon-unix" title="Unix &amp; Linux Stack Exchange"></div><a href="https://unix.stackexchange.com/questions/729308/sed-to-search-and-replace-string-from-another-file" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:106 }); posts_hot_network.click({ item_type:2, location:11 })">
                    sed to search and replace string from another file
                </a>

            </li>
    </ul>

        
</div>

                <div id="feed-link" class="js-feed-link">
        <a href="/feeds/question/9688200" title="Feed of this question and its answers">
            <svg aria-hidden="true" class="fc-orange-400 svg-icon iconRss" width="18" height="18" viewBox="0 0 18 18"><path d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3Zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5V2.5Zm0 5c4.08 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5V7.5Zm0 5c1.36 0 2.5 1.14 2.5 2.5H3v-2.5Z"></path></svg>
            Question feed
        </a>
    </div>
    <aside class="s-modal js-feed-link-modal" tabindex="-1" role="dialog" aria-labelledby="feed-modal-title" aria-describedby="feed-modal-description" aria-hidden="true">
        <div class="s-modal--dialog js-modal-dialog wmx4" role="document" data-controller="se-draggable">
            <h1 class="s-modal--header fw-bold js-first-tabbable c-move" id="feed-modal-title" data-se-draggable-target="handle" tabindex="0">
                Subscribe to RSS
            </h1>
            <div class="d-flex gs4 gsy fd-column">
                <div class="flex--item">
                    <label class="d-block s-label c-default" for="feed-url">
                        Question feed
                        <p class="s-description mt2" id="feed-modal-description">To subscribe to this RSS feed, copy and paste this URL into your RSS reader.</p>
                    </label>
                </div>
                <div class="d-flex ps-relative">
                    <input class="s-input" type="text" name="feed-url" id="feed-url" readonly="readonly" value="https://stackoverflow.com/feeds/question/9688200">
                    <svg aria-hidden="true" class="s-input-icon fc-orange-400 svg-icon iconRss" width="18" height="18" viewBox="0 0 18 18"><path d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3Zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5V2.5Zm0 5c4.08 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5V7.5Zm0 5c1.36 0 2.5 1.14 2.5 2.5H3v-2.5Z"></path></svg>
                </div>
            </div>
            <a class="s-modal--close s-btn s-btn__muted js-modal-close js-last-tabbable" href="#" aria-label="Close">
                <svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14" viewBox="0 0 14 14"><path d="M12 3.41 10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7 12 3.41Z"></path></svg>
            </a>
        </div>
    </aside>

</div>

    </div>
<script>StackExchange.ready(function(){$.get('/posts/9688200/ivc/2516');});</script>
<noscript><div><img src="/posts/9688200/ivc/2516" class="dno" alt="" width="0" height="0"></div></noscript><div style="display:none" id="js-codeblock-lang">default</div></div>


        </div>
    </div>


        
<script type="text/javascript">
    var cam = cam || { opt: {} };
    var clcGamLoaderOptions = cam || { opt: {} };
    var opt = clcGamLoaderOptions.opt;

    opt.omni = 'BP6n57745NoIAAAAAIjUkwACAAAAAgAAAAAAGAAAAHxjKyt8Y3xsaW51eHxkbGx8bGlua2VyfAAejhPULbsfx3O3';

    opt.sf = !0;
    opt.hb = !1;
    opt.ll = !0;
    opt.tlb_position = 0;
    opt.targeting_consent = !1;
    opt.performance_consent = !1;

    opt.targeting = {Registered:['false'],'so-tag':['c_plus_plus','c','linux','dll','linker'],'tag-reportable':['c_plus_plus','c','linux','dll','linker'],'tag-non-reportable':['c_plus_plus','c','linux','dll','linker'],NumberOfAnswers:['5']};
    opt.adReportEnabled = !0;
    opt.adReportUrl = '/ads/report-ad';
    opt.adReportText = 'Report this ad';
	opt.adReportFileTypeErrorMessage = 'Please select a PNG or JPG file.';
    opt.adReportFileSizeErrorMessage = 'The file must be under 2 MiB.';
	opt.adReportErrorText = 'Error uploading ad report.';
	opt.adReportThanksText = 'Thanks for your feedback. We’ll review this against our code of conduct and take action if necessary.';
    opt.adReportLoginExpiredMessage = 'Your login session has expired, please login and try again.';
    opt.adReportLoginErrorMessage = 'An error occurred when loading the report form - please try again';
	opt.adReportModalClass = 'js-ad-report';


    opt.targeting.TargetingConsent = ['False_Passive'];

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('dfptestads')) {
        const dfptestads = urlParams.get('dfptestads');
        opt.targeting.DfpTestAds = dfptestads;
    }
</script>
<script>;(()=>{"use strict";var __webpack_modules__={23:(e,t,o)=>{o.d(t,{Z7:()=>l,eq:()=>r,kG:()=>n});const a=/^\/tags\//.test(location.pathname)||/^\/questions\/tagged\//.test(location.pathname)?"tag-pages":/^\/$/.test(location.pathname)||/^\/home/.test(location.pathname)?"home-page":"question-pages";let s=location.hostname;const i={slots:{lb:[[728,90]],mlb:[[728,90]],smlb:[[728,90]],bmlb:[[728,90]],sb:e=>"dfp-tsb"===e?[[300,250],[300,600]]:[[300,250]],"tag-sponsorship":[[730,135]],"mobile-below-question":[[320,50],[300,250]],msb:[[300,250],[300,600]],"talent-conversion-tracking":[[1,1]],"site-sponsorship":[[230,60]]},ids:{"dfp-tlb":"lb","dfp-mlb":"mlb","dfp-smlb":"smlb","dfp-bmlb":"bmlb","dfp-tsb":"sb","dfp-isb":"sb","dfp-tag":"tag-sponsorship","dfp-msb":"msb","dfp-sspon":"site-sponsorship","dfp-m-aq":"mobile-below-question"},idsToExcludeFromAdReports:["dfp-sspon"]};function n(){return Object.keys(i.ids)}function r(e){return i.idsToExcludeFromAdReports.indexOf(e)<0}function l(e){var t=e.split("_")[0];const o=i.ids[t];let n=i.slots[o];return"function"==typeof n&&(n=n(t)),{path:`/248424177/${s}/${o}/${a}`,sizes:n,zone:o}}},865:(e,t,o)=>{function a(e){return"string"==typeof e?document.getElementById(e):e}function s(e){return!!(e=a(e))&&"none"===getComputedStyle(e).display}function i(e){return!s(e)}function n(e){return!!e}function r(e){return/^\s*$/.test(a(e).innerHTML)}function l(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.display="none"}function d(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.display="none",[].forEach.call(e.children,d)}function c(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.removeProperty("display")}function p(e){const t=document.createElement("script");t.src=e,document.body.appendChild(t)}function g(e){return o=e,(t=[]).push=function(e){return o(),delete this.push,this.push(e)},t;var t,o}function h(e){let t="function"==typeof HTMLTemplateElement;var o=document.createElement(t?"template":"div");return e=e.trim(),o.innerHTML=e,t?o.content.firstChild:o.firstChild}o.d(t,{$Z:()=>c,Bv:()=>h,Gx:()=>p,Nj:()=>a,QZ:()=>g,cf:()=>l,pn:()=>i,wo:()=>d,xb:()=>r,xj:()=>s,yb:()=>n})},763:(__unused_webpack_module,__webpack_exports__,__webpack_require__)=>{__webpack_require__.d(__webpack_exports__,{t:()=>AdReports});var _common_helper__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(865),_console__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(276),_ad_units__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(23);class AdReports{constructor(e,t){if(this.googletag=e,this.cam=t,this.allowedFileTypes=["image/png","image/jpg","image/jpeg"],this.ignoreValidation=!1,_console__WEBPACK_IMPORTED_MODULE_1__.cM("Ad reporting init"),this.cam=t,this.callOnButtonClick=e=>this.onButtonClick(e),this.googletag.pubads().addEventListener("slotRenderEnded",e=>this.handleSlotRendered(e)),Array.isArray(t.slotsRenderedEvents)){_console__WEBPACK_IMPORTED_MODULE_1__.cM("Adding report button to "+t.slotsRenderedEvents.length+" events that have transpired");for(var o=0;o<t.slotsRenderedEvents.length;o++)this.handleSlotRendered(t.slotsRenderedEvents[o])}}handleSlotRendered(e){if(e&&e.slot&&!e.isEmpty&&(e.creativeId||e.lineItemId||!e.isEmpty)){var t=e.slot.getSlotElementId();if(t){var o=document.getElementById(t);if(o)if((0,_ad_units__WEBPACK_IMPORTED_MODULE_0__.eq)(t)){var a=o?.closest(".js-zone-container")?.querySelector(".js-report-ad-button-container");a.append(this.createButton(e)),a.style.height="24px",_console__WEBPACK_IMPORTED_MODULE_1__.cM("Added report button to the bottom of "+t)}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of "+t+": shouldHaveReportButton = false");else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of "+t+": resolved invalid adUnit element")}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of element: invalid adUnitElementId")}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of element: invalid SlotRenderEndedEvent")}async onButtonClick(e){e.preventDefault();let t=e.target;const o=t.dataset.modalUrl,a=t.dataset.googleEventData;return await this.loadModal(o,t,a),!1}createButton(e){let t=document.createElement("button");var o=JSON.stringify(e);return t.dataset.googleEventData=o,t.dataset.modalUrl=this.cam.opt.adReportUrl,t.dataset.adUnit=e.slot.getSlotElementId(),t.classList.add("js-report-ad","s-btn","s-btn__link","fs-fine","mt2","float-right"),t.append(document.createTextNode(this.cam.opt.adReportText)),t.removeEventListener("click",this.callOnButtonClick),t.addEventListener("click",this.callOnButtonClick),t}async loadModal(url,$link,googleEventData){try{await window.StackExchange.helpers.loadModal(url,{returnElements:window.$($link)}),this.initForm(googleEventData)}catch(e){var message="",response=e.responseText?eval(`(${e.responseText})`):null;message=response&&response.isLoggedOut?this.cam.opt.adReportLoginExpiredMessage:this.cam.opt.adReportLoginErrorMessage,window.StackExchange.helpers.showToast(message,{type:"danger"})}}removeModal(){window.StackExchange.helpers.closePopups(document.querySelectorAll("."+this.cam.opt.adReportModalClass),"dismiss")}initForm(e,t=!1){this.ignoreValidation=t,this.$form=document.querySelector(".js-ad-report-form"),this.$googleEventData=this.$form.querySelector(".js-json-data"),this.$adReportReasons=this.$form.querySelectorAll(".js-ad-report-reason"),this.$adReportReasonOther=this.$form.querySelector(".js-ad-report-reason-other"),this.$fileUploaderInput=this.$form.querySelector(".js-file-uploader-input"),this.$imageUploader=this.$form.querySelector(".js-image-uploader"),this.$clearImageUpload=this.$form.querySelector(".js-clear-image-upload"),this.$imageUploaderText=this.$form.querySelector(".js-image-uploader-text"),this.$imageUploaderPreview=this.$form.querySelector(".js-image-uploader-preview"),this.$fileErrorMessage=this.$form.querySelector(".js-file-error");const o=this.$form.querySelector(".js-drag-drop-enabled"),a=this.$form.querySelector(".js-drag-drop-disabled");this.$googleEventData.value=e,this.$adReportReasons.forEach((e,t)=>e.addEventListener("change",e=>{this.$adReportReasonOther.classList.toggle("d-none","3"!==e.target.value)})),this.$fileUploaderInput.addEventListener("change",()=>{this.validateFileInput()&&this.updateImagePreview(this.$fileUploaderInput.files)}),this.$clearImageUpload.addEventListener("click",e=>{e.preventDefault(),this.clearImageUpload()});try{this.$fileUploaderInput[0].value="",this.$imageUploader.addEventListener("dragenter dragover dragleave drop",this.preventDefaults),this.$imageUploader.addEventListener("dragenter dragover",this.handleDragStart),this.$imageUploader.addEventListener("dragleave drop",this.handleDragEnd),this.$imageUploader.addEventListener("drop",this.handleDrop)}catch(e){o.classList.add("d-none"),a.classList.remove("d-none")}this.$form.removeEventListener("",this.handleDragEnd),this.$form.addEventListener("submit",async e=>(e.preventDefault(),this.submitForm(),!1))}clearImageUpload(){this.$fileUploaderInput.value="",this.$imageUploaderPreview.setAttribute("src",""),this.$imageUploaderPreview.classList.add("d-none"),this.$clearImageUpload.classList.add("d-none"),this.$imageUploaderText.classList.remove("d-none"),this.$imageUploader.classList.add("p16","ba","bas-dashed","bc-black-100")}preventDefaults(e){e.preventDefault(),e.stopPropagation()}handleDragStart(e){this.$imageUploader.classList.remove("bas-dashed"),this.$imageUploader.classList.add("bas-solid","bc-black-100")}handleDragEnd(e){this.$imageUploader.classList.remove("bas-solid","bc-black-100"),this.$imageUploader.classList.add("bas-dashed")}handleDrop(e){var t=e.originalEvent.dataTransfer.files;FileReader&&t&&1===t.length&&(this.$fileUploaderInput.files=t,this.validateFileInput()&&this.updateImagePreview(t))}setError(e){this.$fileErrorMessage.parentElement.classList.toggle("has-error",e)}updateImagePreview(e){this.$imageUploader.classList.remove("p16","ba","bas-dashed","bc-black-100"),this.$clearImageUpload.classList.remove("d-none"),this.$imageUploaderText.classList.add("d-none");var t=new FileReader;t.onload=e=>{null!=e.target&&(this.$imageUploaderPreview.setAttribute("src",e.target.result),this.$imageUploaderPreview.classList.remove("d-none"))},t.readAsDataURL(e[0])}validateFileInput(){if(this.ignoreValidation)return!0;const e=this.cam.opt.adReportFileTypeErrorMessage,t=this.cam.opt.adReportFileSizeErrorMessage;if(null==this.$fileUploaderInput.files)return!1;var o=this.$fileUploaderInput.files[0];return null==o?(this.setError(!0),!1):this.allowedFileTypes.indexOf(o.type)<0?(this.$fileErrorMessage.textContent=e,this.$fileErrorMessage.classList.remove("d-none"),this.setError(!0),!1):o.size>2097152?(this.$fileErrorMessage.textContent=t,this.$fileErrorMessage.classList.remove("d-none"),this.setError(!0),!1):(this.$fileErrorMessage.classList.add("d-none"),this.setError(!1),!0)}async submitForm(){if(!this.validateFileInput())return!1;this.$form.querySelector("[type=submit]").setAttribute("disabled","true");var e=JSON.parse(this.$googleEventData.value||"{}");e.Reason=parseInt(this.$form.querySelector(".js-ad-report-reason:checked").value,10),e.Description=this.$adReportReasonOther.value,this.$googleEventData.value=JSON.stringify(e);var t=new FormData(this.$form);try{const e=await window.fetch(this.$form.getAttribute("action"),{method:this.$form.getAttribute("method"),body:t,cache:"no-cache"}),a=e.headers.get("content-type")||"",s=await e.text();if(!e.ok)throw new Error("response not valid");if(0===a.indexOf("text/html")){var o=(0,_common_helper__WEBPACK_IMPORTED_MODULE_2__.Bv)(s);const e=o?o.querySelector(".js-modal-content"):null;if(_console__WEBPACK_IMPORTED_MODULE_1__.cM("$popupContent"),_console__WEBPACK_IMPORTED_MODULE_1__.cM(e),!e)throw new Error(`Could not find .js-modal-content in response from ${this.$form.getAttribute("action")}`);document.querySelector(".js-modal-content").replaceWith(e)}else window.StackExchange.helpers.showToast(this.cam.opt.adReportThanksText,{type:"success"}),this.removeModal()}catch(e){window.StackExchange.helpers.showToast(this.cam.opt.adReportErrorText,{type:"danger"})}finally{let e=this.$form.querySelector("[type=submit]");e&&e.removeAttribute("disabled")}}}},276:(e,t,o)=>{function a(...e){}o.d(t,{cM:()=>a})}},__webpack_module_cache__={};function __webpack_require__(e){var t=__webpack_module_cache__[e];if(void 0!==t)return t.exports;var o=__webpack_module_cache__[e]={exports:{}};return __webpack_modules__[e](o,o.exports,__webpack_require__),o.exports}__webpack_require__.d=(e,t)=>{for(var o in t)__webpack_require__.o(t,o)&&!__webpack_require__.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:t[o]})},__webpack_require__.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t);var __webpack_exports__={};(()=>{var e=__webpack_require__(276),t=(e=>(e[e.Above=0]="Above",e[e.Below=1]="Below",e))(t||{});const o=Object.assign({},{"lib":"https://cdn.sstatic.net/clc/js/bundles/gam_loader_script/gam_loader_script.bundle.741.0a8355d1d041eee31b72.min.js","style":null,"u":null,"wa":true,"kt":2000,"tto":true,"h":"clc.stackoverflow.com","allowed":"^(((talent\\.)?stackoverflow)|(blog\\.codinghorror)|(.*\\.googlesyndication)|(serverfault|askubuntu)|([^\\.]+\\.stackexchange))\\.com$","wv":true,"al":false,"abd":true,"cpa_liid":[5882654614],"cpa_cid":[138377597667],"dp":false});var a=__webpack_require__(23),s=__webpack_require__(865),i=__webpack_require__(763);window.cam=new class{constructor(){this.gptImported=!1,this.collapsed={},e.cM("constructor"),this.clc_options=o,window.clcGamLoaderOptions?Object.assign(this,window.clcGamLoaderOptions):void 0===this.opt&&(this.opt=window.opt)}init(){if(e.cM("init"),void 0===this.opt)throw new Error("opt not set, required by GAM Loader");e.cM("setup message handler"),window.addEventListener("message",e=>{this.onmessage(e)})}handleSlotRenderedNoAdReport(){if(googletag.pubads().addEventListener("slotRenderEnded",e=>this.applyExtraMarginBottom(e)),Array.isArray(this.slotsRenderedEvents))for(var e=0;e<this.slotsRenderedEvents.length;e++)this.applyExtraMarginBottom(this.slotsRenderedEvents[e])}onmessage(t){let o="omni";if(t.data&&("string"==typeof t.data||t.data instanceof String))if(0===t.data.indexOf("get-omni-")){e.cM("Recevied get-omni message, sending back omni");var a=t.source,i=this.opt.omni,n="string"==typeof i?i:"";a.postMessage([o,n].join("|"),"*")}else if(0===t.data.indexOf("collapse-")){e.cM("Recevied collapse message, collapse ad iframe"),e.cM(t);for(var r=t.source.window,l=document.getElementsByTagName("IFRAME"),d=0;d<l.length;d++){var c=l[d];if(c.contentWindow==r)return void(0,s.wo)(c.parentElement.parentElement.parentElement)}}else if(0===t.data.indexOf("resize|")){e.cM("Recevied resize message, resize ad iframe"),e.cM(t);let o=this._getFrameByEvent(t),a=t.data.split("|"),s=parseFloat(a[1])+.5;e.cM("New iframe height "+s),o.height=s.toString(),o.parentElement.style.height=s.toString()+"px"}}_getFrameByEvent(e){return Array.from(document.getElementsByTagName("iframe")).filter(t=>t.contentWindow===e.source)[0]}classifyZoneIds(e){const t=e.map(s.Nj).filter(s.yb);return{eligible:t.filter(s.xb).filter(s.pn),ineligible:t.filter(s.xj)}}applyExtraMarginBottom(t){if(t&&t.slot&&!t.isEmpty&&(t.creativeId||t.lineItemId||!t.isEmpty)){var o=t.slot.getSlotElementId();if(o){var s=document.getElementById(o);if(s)if((0,a.eq)(o)){var i=s?.closest(".js-zone-container");i.style.marginBottom="24px",e.cM("Applied extra margin to the bottom of "+o)}else e.cM("Not applying extra margin to the bottom of "+o+": shouldHaveReportButton = false");else e.cM("Not applying extra margin to the bottom of "+o+": resolved invalid adUnit element")}else e.cM("Not applying extra margin to the bottom of element: invalid adUnitElementId")}else e.cM("Not applying extra margin to the bottom of element: invalid SlotRenderEndedEvent")}load(o=(0,a.kG)()){const n=this.opt.tlb_position===t.Above?["dfp-mlb","dfp-smlb"]:["dfp-mlb","dfp-smlb","dfp-tlb"];if(!this.isGptReady())return e.cM("Initializing..."),this.initGpt(),void googletag.cmd.push(()=>this.load(o));this.opt.adReportEnabled?(e.cM("Ad reporting enabled"),this.adReports=new i.t(googletag,this)):(e.cM("Ad reporting not enabled"),this.handleSlotRenderedNoAdReport()),e.cM("Attempting to load ads into ids: ",o);const{eligible:r,ineligible:l}=this.classifyZoneIds(o);if(this.initDebugPanel(googletag,r.concat(l)),r.forEach(e=>(0,s.cf)(e)),l.forEach(s.wo),0!==r.length){e.cM("Eligible ids:",r),this.opt.abd&&this.appendAdblockDetector();var d=googletag.pubads().getSlots().filter(e=>o.indexOf(e.getSlotElementId())>=0);googletag.destroySlots(d),this.opt.sf&&(googletag.pubads().setForceSafeFrame(!0),googletag.pubads().setSafeFrameConfig({allowOverlayExpansion:!0,allowPushExpansion:!0,sandbox:!0})),e.cM("Targeting consent: Checking..."),void 0!==this.opt.targeting_consent&&(e.cM("Targeting consent: Parameter set"),e.cM("Targeting consent: Consent given? ",this.opt.targeting_consent),googletag.pubads().setRequestNonPersonalizedAds(this.opt.targeting_consent?0:1),this.opt.targeting_consent||googletag.pubads().setPrivacySettings({limitedAds:!0})),this.opt.ll||googletag.pubads().enableSingleRequest(),cam.sreEvent||(googletag.pubads().addEventListener("slotRenderEnded",e=>this.onSlotRendered(e)),cam.sreEvent=!0),this.setTargeting(googletag);var c=r.filter(e=>!this.opt.ll||n.indexOf(e.id)<0),p=r.filter(e=>!!this.opt.ll&&n.indexOf(e.id)>=0);e.cM("Up front ids:",c),e.cM("Lazy loaded ids:",p),c.forEach(t=>{e.cM(`Defining ad for element ${t.id}`),this.defineSlot(t.id,googletag),t.setAttribute("data-dfp-zone","true")}),googletag.enableServices(),c.forEach(t=>{e.cM(`Displaying ad for element ${t.id}`),googletag.cmd.push(()=>googletag.display(t.id))}),this.opt.ll&&(e.cM("Enabling lazy loading for GAM"),googletag.pubads().enableLazyLoad({fetchMarginPercent:0,renderMarginPercent:0}),e.cM("Setting up lazy loaded ad units"),p.forEach(t=>{e.cM(`Lazy loading - Defining Slot ${t.id}`),this.defineSlot(t.id,googletag)}),p.forEach(t=>{e.cM(`Lazy loading - Displaying ad for element ${t.id}`),googletag.cmd.push(()=>googletag.display(t.id))}))}else e.cM("Found no ad ids on page")}setTargeting(t){let o=this.opt.targeting;if(!o)throw new Error("Targeting not defined");"SystemDefault"===o.ProductVariant&&(window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches?o.ProductVariant="Dark":o.ProductVariant="Light"),Object.keys(o).forEach(a=>{e.cM(`-> targeting - ${a}: ${o[a]}`),t.pubads().setTargeting(a,o[a])})}appendAdblockDetector(){const e=document.createElement("div");e.className="adsbox",e.id="clc-abd",e.style.position="absolute",e.style.pointerEvents="none",e.innerHTML="&nbsp;",document.body.appendChild(e)}onSlotRendered(o){try{const n=o.slot.getSlotElementId();let r=[];n||r.push("id=0");const l=document.getElementById(n);if(n&&!l&&r.push("el=0"),0!==r.length)return void this.stalled(r.join("&"));const{path:d,sizes:c,zone:p}=(0,a.Z7)(n);if(this.collapsed[p]&&o.isEmpty)return e.cM(`No line item for the element #${l.id}... collapsing.`),void(0,s.wo)(l);if(this.slotsRenderedEvents.push(o),o.lineItemId||o.creativeId||!o.isEmpty){e.cM(`Rendered ad for element #${l.id} [line item #${o.lineItemId}]`),e.cM(o);var i=l.parentElement;if(i.classList.contains("js-zone-container")){switch((0,s.cf)(i),n){case"dfp-tlb":this.opt.tlb_position===t.Above?i.classList.add("mb8"):i.classList.add("mt16");break;case"dfp-tag":i.classList.add("mb8");break;case"dfp-msb":i.classList.add("mt16");break;case"dfp-mlb":case"dfp-smlb":case"dfp-bmlb":i.classList.add("my8");break;case"dfp-isb":i.classList.add("mt24");break;case"dfp-m-aq":i.classList.add("my12"),i.classList.add("mx-auto")}(0,s.$Z)(i),(0,s.$Z)(l)}else e.cM(`No ad for element #${l.id}, collapsing`),e.cM(o),(0,s.wo)(l)}}catch(e){this.stalled("e=1")}}stalled(e){(new Image).src=`https://${this.clc_options.h}/stalled.gif?${e}`}defineSlot(t,o){"dfp-isb"===t&&(e.cM("-> targeting - Sidebar: Inline"),o.pubads().setTargeting("Sidebar",["Inline"])),"dfp-tsb"===t&&(e.cM("-> targeting - Sidebar: Right"),o.pubads().setTargeting("Sidebar",["Right"]));const{path:s,sizes:i,zone:n}=(0,a.Z7)(t);e.cM(`Defining slot for ${t}: ${s}, sizes: ${JSON.stringify(i)}`),o.defineSlot(s,i,t).addService(o.pubads())}importGptLibrary(){this.gptImported||(this.gptImported=!0,void 0===this.opt.targeting_consent||this.opt.targeting_consent?(0,s.Gx)("https://securepubads.g.doubleclick.net/tag/js/gpt.js"):(0,s.Gx)("https://pagead2.googlesyndication.com/tag/js/gpt.js"))}isGptReady(){return"undefined"!=typeof googletag&&!!googletag.apiReady}initGpt(){"undefined"==typeof googletag&&(window.googletag={cmd:(0,s.QZ)(()=>this.importGptLibrary())})}initDebugPanel(t,o){e.cM("initDebugPanel"),e.cM("Not showing debug panel")}},window.clcGamLoaderOptions&&(cam.init(),cam.load())})()})();</script><script src="https://pagead2.googlesyndication.com/tag/js/gpt.js"></script>
        
    <footer id="footer" class="site-footer js-footer" role="contentinfo">
        <div class="site-footer--container">
                <div class="site-footer--logo">

                    <a href="https://stackoverflow.com" aria-label="Stack Overflow"><svg aria-hidden="true" class="native svg-icon iconLogoGlyphMd" width="32" height="37" viewBox="0 0 32 37"><path d="M26 33v-9h4v13H0V24h4v9h22Z" fill="#BCBBBB"></path><path d="m21.5 0-2.7 2 9.9 13.3 2.7-2L21.5 0ZM26 18.4 13.3 7.8l2.1-2.5 12.7 10.6-2.1 2.5ZM9.1 15.2l15 7 1.4-3-15-7-1.4 3Zm14 10.79.68-2.95-16.1-3.35L7 23l16.1 2.99ZM23 30H7v-3h16v3Z" fill="#F48024"></path></svg></a>
                </div>
            <nav class="site-footer--nav">
                    <div class="site-footer--col">
                        <h5 class="-title"><a href="https://stackoverflow.com" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 15})">Stack Overflow</a></h5>
                        <ul class="-list js-primary-footer-links">
                            <li><a href="/questions" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 16})">Questions</a></li>
                                <li><a href="/help" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 3 })">Help</a></li>
                        </ul>
                    </div>
                    <div class="site-footer--col">
                        <h5 class="-title"><a href="https://stackoverflow.co/" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 19 })">Products</a></h5>
                        <ul class="-list">
                            <li><a href="https://stackoverflow.co/teams" class="js-gps-track -link" data-ga="[&quot;teams traffic&quot;,&quot;footer - site nav&quot;,&quot;stackoverflow.com/teams&quot;,null,{&quot;dimension4&quot;:&quot;teams&quot;}]" data-gps-track="footer.click({ location: 2, link: 29 })">Teams</a></li>
                            <li><a href="https://stackoverflow.co/advertising" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 21 })">Advertising</a></li>
                            <li><a href="https://stackoverflow.co/collectives" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 40 })">Collectives</a></li>
                            <li><a href="https://stackoverflow.co/talent" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 20 })">Talent</a></li>
                        </ul>
                    </div>
                <div class="site-footer--col">
                    <h5 class="-title"><a class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">Company</a></h5>
                    <ul class="-list">
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">About</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 27 })" href="https://stackoverflow.co/company/press">Press</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 9 })" href="https://stackoverflow.co/company/work-here">Work Here</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 7 })" href="https://stackoverflow.com/legal">Legal</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 8 })" href="https://stackoverflow.com/legal/privacy-policy">Privacy Policy</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 37 })" href="https://stackoverflow.com/legal/terms-of-service">Terms of Service</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 13 })" href="https://stackoverflow.co/company/contact">Contact Us</a></li>
                            <li class="" id="consent-footer-link"><a class="js-gps-track -link js-cookie-settings" data-gps-track="footer.click({ location: 2, link: 38 })" href="#" data-consent-popup-loader="footer">Cookie Settings</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 39 })" href="https://stackoverflow.com/legal/cookie-policy">Cookie Policy</a></li>
                    </ul>
                </div>
                <div class="site-footer--col site-footer--categories-nav">
                    <div>
                        <h5 class="-title"><a href="https://stackexchange.com" data-gps-track="footer.click({ location: 2, link: 30 })">Stack Exchange Network</a></h5>
                        <ul class="-list">
                            <li>
                                <a href="https://stackexchange.com/sites#technology" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Technology
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#culturerecreation" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Culture &amp; recreation
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#lifearts" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Life &amp; arts
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#science" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Science
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#professional" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Professional
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#business" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Business
                                </a>
                            </li>

                            <li class="mt16 md:mt0">
                                <a href="https://api.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    API
                                </a>
                            </li>

                            <li>
                                <a href="https://data.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Data
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="site-footer--copyright fs-fine md:mt24">
                <ul class="-list -social md:mb8">
                    <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link:4 })" href="https://stackoverflow.blog?blb=1">Blog</a></li>
                    <li><a href="https://www.facebook.com/officialstackoverflow/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 31 })">Facebook</a></li>
                    <li><a href="https://twitter.com/stackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 32 })">Twitter</a></li>
                    <li><a href="https://linkedin.com/company/stack-overflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 33 })">LinkedIn</a></li>
                    <li><a href="https://www.instagram.com/thestackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 36 })">Instagram</a></li>
                </ul>

                <p class="md:mb0">
Site design / logo © 2022 Stack Exchange Inc; user contributions licensed under <span class="td-underline"><a href="https://stackoverflow.com/help/licensing">CC BY-SA</a></span>.                    <span id="svnrev">rev&nbsp;2022.12.21.43127</span>
                </p>
            </div>
        </div>

    </footer>


                <!-- Google tag (gtag.js) -->
            <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-WCZ03SZFCQ"></script>
            <script>
                window.dataLayer = window.dataLayer || [];
                function gtag() { dataLayer.push(arguments); }
            </script>
        <script>
            StackExchange.ready(function() {

                var ga3Settings = {
                    autoLink: ["stackoverflow.blog","info.stackoverflowsolutions.com","stackoverflowsolutions.com"],
                    sendTitles: true,
                    tracker: window.ga,
                    trackingCodes: [
                        'UA-108242619-1'
                    ],
                    checkDimension: 'dimension42'
                                                    };

                var customGA4Dimensions = {};


                var ga4Settings = {
                    tracker: gtag,
                    trackingCodes: [
                        'G-WCZ03SZFCQ'
                    ],
                    consentsToPerformanceCookies: "denied",
                    consentsToTargetingCookies: "denied",
                    eventParameters: customGA4Dimensions,
                    checkForAdBlock: true
                };

                StackExchange.ga.init({ GA3: ga3Settings, GA4: ga4Settings });


                StackExchange.ga.setDimension('dimension2', '|c&#x2B;&#x2B;|c|linux|dll|linker|');


                StackExchange.ga.setDimension('dimension3', 'Questions/Show');


                StackExchange.ga.setDimension('dimension7', "1671808623.1076742737");

                StackExchange.ga.trackPageView();
            });
        </script><iframe src="https://6069a9ccde7913e3c1d8e794842d62f0.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html" style="visibility: hidden; display: none;"></iframe>

        
                <div class="ff-sans ps-fixed z-nav-fixed ws4 sm:w-auto p32 sm:p16 bg-black-750 fc-white bar-lg b16 l16 r16 js-consent-banner" style="display: none;">
                    <svg aria-hidden="true" class="mln4 mb24 sm:d-none svg-spot spotCookieLg" style="color: var(--theme-button-filled-background-color)" width="96" height="96" viewBox="0 0 96 96">
                        <path d="M35 45.5a7.5 7.5 0 11-15 0 7.5 7.5 0 0115 0zM63.5 63a7.5 7.5 0 100-15 7.5 7.5 0 000 15zm-19 19a7.5 7.5 0 100-15 7.5 7.5 0 000 15z" opacity=".2"></path>
                        <path d="M56.99 2.53a23.1 23.1 0 0114.66 6.15h.01l.01.02c.57.55.61 1.27.5 1.74v.07a10.95 10.95 0 01-3.07 4.77 9 9 0 01-6.9 2.5 10.34 10.34 0 01-9.72-10.44v-.08a10 10 0 011.03-3.74l.01-.03.02-.02c.28-.5.82-.92 1.52-.95.63-.02 1.27-.02 1.93.01zm12.04 7.83a20.1 20.1 0 00-12.2-4.83l-.92-.03c-.23.6-.38 1.25-.43 1.94a7.34 7.34 0 006.95 7.34 6 6 0 004.64-1.7c.94-.88 1.6-1.9 1.96-2.72zm15.3 8.76a6.84 6.84 0 00-5.09-.24 7.9 7.9 0 00-3.28 2.05 1.8 1.8 0 00-.3 1.95l.02.02v.02a15.16 15.16 0 008.74 7.47c.64.23 1.32.08 1.8-.33a6.63 6.63 0 001.63-1.97l.01-.03.01-.03c1.67-3.5-.12-7.32-3.54-8.91zm-5.5 3.28c.36-.25.82-.5 1.35-.67.92-.3 1.92-.35 2.89.1 2.14 1 2.92 3.14 2.11 4.88-.12.21-.26.41-.43.6l-.26-.1a12.29 12.29 0 01-5.66-4.81zM32 24a2 2 0 11-4 0 2 2 0 014 0zm12 21a2 2 0 11-4 0 2 2 0 014 0zm36 4a2 2 0 11-4 0 2 2 0 014 0zm-7 21a2 2 0 11-4 0 2 2 0 014 0zM59 81a2 2 0 11-4 0 2 2 0 014 0zM22 63a2 2 0 11-4 0 2 2 0 014 0zm27 7a9 9 0 11-18 0 9 9 0 0118 0zm-3 0a6 6 0 10-12 0 6 6 0 0012 0zM33 41a9 9 0 11-18 0 9 9 0 0118 0zm-15 0a6 6 0 1012 0 6 6 0 00-12 0zm50 11a9 9 0 11-18 0 9 9 0 0118 0zm-3 0a6 6 0 10-12 0 6 6 0 0012 0zM44.08 4.24c.31.48.33 1.09.05 1.58a17.46 17.46 0 00-2.36 8.8c0 9.55 7.58 17.24 16.85 17.24 2.97 0 5.75-.78 8.16-2.15a1.5 1.5 0 012.1.66 12.08 12.08 0 0011 6.74 12.4 12.4 0 007.85-2.75 1.5 1.5 0 012.38.74A45.76 45.76 0 0192 48.16c0 24.77-19.67 44.9-44 44.9S4 72.93 4 48.16C4 25.23 20.84 6.28 42.64 3.58a1.5 1.5 0 011.44.66zM40.22 7C21.32 10.71 7 27.7 7 48.16c0 23.17 18.39 41.9 41 41.9s41-18.73 41-41.9c0-3.52-.42-6.93-1.22-10.2a15.5 15.5 0 01-7.9 2.15c-5.5 0-10.36-2.83-12.97-7.1a19.46 19.46 0 01-8.28 1.85c-11 0-19.86-9.1-19.86-20.24 0-2.7.52-5.26 1.45-7.62zM92 91a2 2 0 100-4 2 2 0 000 4zM7 8.5a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0zM82.5 90a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm9.5-7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM13.5 8a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM80 14.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM53.5 20a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
                    </svg>
                    <p class="fs-body2 fw-bold mb4">
                        Your privacy
                    </p>
                    <p class="mb16 s-anchors s-anchors__inherit s-anchors__underlined">
                        By clicking “Accept all cookies”, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our <a href="https://stackoverflow.com/legal/cookie-policy">Cookie Policy</a>.
                    </p>
                    <div class="d-flex gs8 ai-stretch fd-column sm:fd-row">
                        <button class="flex--item s-btn s-btn__primary js-accept-cookies js-consent-banner-hide">
                            Accept all cookies
                        </button>

                        <button class="flex--item s-btn s-btn__filled js-cookie-settings" data-consent-popup-loader="banner">
                            Customize settings
                        </button>
                    </div>
                </div>
    <div id="onetrust-consent-sdk" class="d-none"><div class="onetrust-pc-dark-filter ot-hide ot-fade-in"></div></div>
    <div id="onetrust-banner-sdk" data-controller="s-modal"></div>
    <div id="ot-pc-content" class="d-none"></div>
    
    <div class="d-none js-consent-banner-version" data-consent-banner-version="baseline"></div>

    
    
    
<iframe name="google_ads_top_frame" id="google_ads_top_frame" style="display: none; position: fixed; left: -999px; top: -999px; width: 0px; height: 0px;"></iframe><script type="text/javascript" charset="UTF-8" data-domain-script="c3d9f1e3-55f3-4eba-b268-46cee4c6789c" async="true" src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js"></script><iframe src="https://tpc.googlesyndication.com/sodar/sodar2/225/runner.html" width="0" height="0" style="display: none;"></iframe></body></html>