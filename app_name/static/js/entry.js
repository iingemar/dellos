var content = require("./content.js");
var otherContent = require("./otherContent.js");

document.write(content + otherContent);

// Test underscore plugin
console.log(_.first([5, 4, 3, 2, 1]));

// Test Backbone
var IndexView = Backbone.View.extend({
    el: $('#backbone-content'),

    events: {
        'click .btn': 'click'
    },

    render: function(){
        console.log('render');
    },

    click: function() {
        console.log('click');
    }
});


var indexView = new IndexView();

indexView.render();