function setLanguage(lang){

    localStorage.setItem("lang", lang);

    updateLanguage();
}

function updateLanguage(){

    let lang = localStorage.getItem("lang") || "en";

    // UI TRANSLATIONS
    const translations = {

        en:{
            title:"🌿 Mahoba Organic Market",
            cart:"Cart",
            shops:"Shops",
            addtocart:"Add to Cart",
            buynow:"Buy Now",
            payment:"Payment",
            search:"Search",
            browse:"Browse Shops",
            products:"Products",
            allshops:"All Shops",
            shopproducts:"Shop Products",

            view:"View",
            visit:"Visit",
            filter:"Filter",
            sort:"Sort Low → High",

            heroheading:"Fresh • Organic • Local",

            herotext:"Compare prices across shops and buy the best quality groceries.",

            featuredshops:"Featured Shops",

            popularshops:"Popular Shops",

            seller:"Trusted local seller",
            emptycart:"Your cart is empty",
            emptycartdesc:"Add fresh organic products from local shops.",
            exploreshops:"Explore Shops",
            allshops:"All Shops"
        },

        hi:{
            title:"🌿 महोबा ऑर्गेनिक मार्केट",
            emptycart:"आपकी कार्ट खाली है",
            emptycartdesc:"लोकल दुकानों से ताज़ा ऑर्गेनिक उत्पाद जोड़ें।",
            exploreshops:"दुकानें देखें",
            allshops:"सभी दुकानें",
            cart:"कार्ट",
            shops:"दुकानें",
            addtocart:"कार्ट में जोड़ें",
            buynow:"अभी खरीदें",
            payment:"भुगतान",
            search:"खोजें",
            browse:"दुकान देखें",
            products:"उत्पाद",
            allshops:"सभी दुकानें",
            shopproducts:"दुकान के उत्पाद",

            view:"देखें",
            visit:"जाएँ",
            filter:"फ़िल्टर",
            sort:"कम कीमत → अधिक कीमत",

            heroheading:"ताज़ा • ऑर्गेनिक • स्थानीय",

            herotext:"दुकानों के बीच कीमतों की तुलना करें और सर्वोत्तम गुणवत्ता का सामान खरीदें।",

            featuredshops:"विशेष दुकानें",

            popularshops:"लोकप्रिय दुकानें",

            seller:"विश्वसनीय स्थानीय विक्रेता"
        }
    };

    // CHANGE UI TEXT
    document.querySelectorAll("[data-key]").forEach(el=>{

        let key = el.getAttribute("data-key");

        if(translations[lang][key]){
            el.innerText = translations[lang][key];
        }
    });

    // CHANGE PRODUCT NAMES
    document.querySelectorAll(".product-name").forEach(el=>{

        if(lang === "hi"){
            el.innerText = el.dataset.hi;
        }
        else{
            el.innerText = el.dataset.en;
        }
    });
}
document.addEventListener(
    "DOMContentLoaded",
    updateLanguage
);
