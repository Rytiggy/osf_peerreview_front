import Model from "ember-data/model";
import attr from "ember-data/attr";
import Ember from "ember";
export default Model.extend( {
    conference: attr( 'string' ),
    title: attr( 'string' ),
    reviewdeadline: attr( 'string' ),
    author_name: attr( 'string' ),
    author_email: attr( 'string' ),
    status: attr( 'string' ),
    link: attr( 'string' ),
    attachment: attr( 'string' ),
    iswaiting: Ember.computed.equal( 'status', 'Awaiting review' ),
    isdeclined: Ember.computed.equal( 'status', 'Declined' )
} );
