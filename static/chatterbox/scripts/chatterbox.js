

const cbx = document.getElementById("chatterbox");

const delete_cbx = () => {
  let i = 2; //think child elements might start at 0, 2 seems to work for deletion down to 3 total
  while (i < cbx.childElementCount) {
    let node_rem = cbx.lastChild;
    cbx.removeChild(node_rem);
  }
}

/// profile elements

class PenguinProfile {
  constructor(name, sub, temperature, image_file) {
    this.name = name;
    this.sub = sub;
    this.image_file = image_file;
    this.temperature = temperature; // unpredictability... i.e., penguin identity based on ML results
  }

  get chat_post() {
    return make_a_chat_post();
  }

  fetch_a_json() {

    let request = new XMLHttpRequest();
    request.open("GET", `./static/chatterbox/texts/${this.sub}_${this.temperature}.json`, false);
    request.send(null);
    let json_source = JSON.parse(request.responseText);
    //and now to fetch the dynamic multiplier to pass to random:
    let json_size = Object.keys(json_source);
    let array_s = json_size.length;
    
    let random_string_fetch_int =  Math.floor((Math.random() * parseInt(`${array_s}`)));

    let string_return = json_source[random_string_fetch_int];
    return string_return;

  }

  make_a_chat_post() {
    
    let div_slice = document.createElement("div");
    div_slice.classList.add("chatWithinWindow");
    
    let chat_img = div_slice.appendChild(document.createElement("img"));
    chat_img.src = this.image_file;
    
    let p = document.createElement("p");
    p.classList.add("text-left");
    p.classList.add("astroTextNoPad");
    let node = document.createTextNode(":: " + this.fetch_a_json()); //insert json data here
    p.appendChild(node);
    div_slice.appendChild(p);


    const name_stamp = document.createElement("span");
    name_stamp.classList.add("text-left");
    name_stamp.classList.add("nameAvatar");
    let name_node = document.createTextNode(`> ${this.name}`);
    name_stamp.appendChild(name_node);
    div_slice.appendChild(name_stamp);
    
    const time_stamp = document.createElement("span");
    time_stamp.classList.add("timeStamp");
    let time_node = document.createTextNode(`${Math.floor(Math.random() * 10)}:${Math.floor(Math.random() * 10)}`);
    time_stamp.appendChild(time_node);
    div_slice.appendChild(time_stamp);

    cbx.prepend(div_slice);
  }
}

const CadetChubbins = new PenguinProfile("Cadet Chubbin Nuggets", "VXJunkies", "medium_high", "./static/chatterbox/images/cadetpenguinman.jpg")




//function to pick random penguin to add to chat

setInterval(() => {
  
  delete_cbx();
  CadetChubbins.make_a_chat_post();
  //delete_cbx();

}, 5000);
