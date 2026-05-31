/*
Dictionary search module

Features:
- English ↔ Ukrainian search
- Instant filtering while typing
- Exact match prioritization
- Result limiting
- Clear search button
*/

<div class="search-box">

<input type="text" id="search"
placeholder="Введіть слово:">

<span id="clearBtn">✕</span>

</div>

<div id="results"></div>

<a href="/" class="link-btn_home">НА ГОЛОВНУ</a>

</div>

<script src="{% static 'js/search.js' %}"></script>

<script>

const searchInput = document.getElementById("search");
const resultsBox = document.getElementById("results");
const clearBtn = document.getElementById("clearBtn");

searchInput.addEventListener("keyup", function(){

let value = this.value.toLowerCase();
resultsBox.innerHTML = "";

if(value.length < 1) return;

let results = dictionary
.filter(word =>
word.en.toLowerCase().includes(value) ||
word.ua.toLowerCase().includes(value)
)
.sort((a,b)=>{

let aExact =
a.en.toLowerCase()===value ||
a.ua.toLowerCase()===value;

let bExact =
b.en.toLowerCase()===value ||
b.ua.toLowerCase()===value;

return bExact-aExact;

});

results.slice(0,20).forEach(word=>{

let div=document.createElement("div");

div.innerHTML=
"<div style='font-size:50px; margin:25px 0; color:#0B3D91'>" +
word.ua+" - <b>"+word.en+"</b> - "+word.tr+
"</div>";
resultsBox.appendChild(div);

});

});

searchInput.addEventListener("input", function(){
clearBtn.style.display = this.value ? "block" : "none";
});

clearBtn.addEventListener("click", function(){
searchInput.value="";
clearBtn.style.display="none";
resultsBox.innerHTML="";
searchInput.focus();
});

</script>
