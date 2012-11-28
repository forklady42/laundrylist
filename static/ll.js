function viewCloset(category) {
    console.log("inserting items")
    $.getJSON("/closet/view/"+category, function(data) {
        var items = ""
        console.log('JSON')
        
        $.each(data, function() {
            items += "<h3>" + this['item'] + 
                "</h3><div><p>";
            if (this['color']) {
                items += "<b>Color:</b> " + this['color'] + "</br>" };
            if (this['brand']) {
                items += "<b>Brand: </b>" + this['brand'] + "</br>" };
            if (this['price']) {
                items += "<b>Price:</b> " + this['price'] + "</br>" };
            if (this['worn'].length > 0) {
                items += "<b> Dates worn: </b></br>"
                //recursive function here? (i.e. functional-eqse)
                for (var i = 0; i < this['worn'].length; i++) {
                    items += this['worn'][i] + "</br>"
                    };
                }
            items += "</p></div>"
        });
        
        $("#items").html(items); 
        $("#items").accordion({
            collapsible: true,
            heightStyle: "content"
        });        
    });
}

$(document).ready(function(){
    $('#form').submit(function(){
        viewCloset($('form').serializeArray()[1]["value"]);
        return false;
    }); 
});    

    