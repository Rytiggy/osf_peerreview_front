import Ember from 'ember';
export default Ember.Component.extend({
  didRender(){
  Ember.$(".ptitle h1").text(this.get('title'));
  },
  actions: {
  filterdata(){
  this.sendAction('filterdata');
    if(this.get('filter') === false){
      Ember.$(".filter-control-holder").hide();
    }
  }
});
