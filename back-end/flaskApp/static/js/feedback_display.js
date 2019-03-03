function feedbackCard(title, speakers, spRating, cntRating, comments)
{
    var col_div = document.createElement("div");
    var card_div = document.createElement("div");
    var card_content_div = document.createElement("div");
    var title_h2 = document.createElement("h2");
    var speakers_h4 = document.createElement("h4");
    var sp_rating_p = document.createElement("p");
    var cnt_rating_p = document.createElement("p");
    var sp_rating_span = document.createElement("span");
    var cnt_rating_span = document.createElement("span");

    sp_rating_span.setAttribute("name","speaker-rating");
    sp_rating_span.setAttribute("id","speaker-rating");
    sp_rating_span.innerText = spRating;
    cnt_rating_span.setAttribute("name", "content-rating");
    cnt_rating_span.setAttribute("id", "content-rating");
    cnt_rating_span.innerText = cntRating;

    cnt_rating_p.innerText = "Content rating: ";
    cnt_rating_p.className += "ratings";
    sp_rating_p.innerText = "Speaker rating: ";
    sp_rating_p.className += "ratings";

    speakers_h4.innerText = speakers;
    title_h2.innerText = title;

    card_content_div.className += "card-content";
    card_div.className += "card";
    col_div.className += "col s12 m6";

    sp_rating_p.appendChild(sp_rating_span);
    cnt_rating_p.appendChild(cnt_rating_span);

    card_content_div.appendChild(title_h2);
    card_content_div.appendChild(speakers_h4);
    card_content_div.appendChild(sp_rating_p);
    card_content_div.appendChild(cnt_rating_p);
    card_div.appendChild(card_content_div);
    col_div.appendChild(card_div);

    document.getElementById("feedback-div").appendChild(col_div);
}


feedbackCard("title", "author", "4", "3");