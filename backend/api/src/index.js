'use strict';


const AWS = require('aws-sdk');
const dynamo = new AWS.DynamoDB.DocumentClient();

const tableName = process.env.TABLE_NAME;

const createResponse = (statusCode, body) => ({ statusCode, body });

function simple_get(event, ident, callback) {
    
    let params = {
        TableName: tableName,
        Key: {
            id: ident
        }
    };
    
    let dbGet = (params) => { return dynamo.get(params).promise() };
    
    dbGet(params).then( (data) => {
        if (!data.Item) {
            callback(null, createResponse(404, "ITEM NOT FOUND"));
            return;
        }
        console.log(`RETRIEVED ITEM SUCCESSFULLY WITH doc = ${data.Item.doc}`);
        callback(null, createResponse(200, data.Item.doc));
    }).catch( (err) => { 
        console.log(`GET ITEM FAILED FOR doc = ${params.Key.id}, WITH ERROR: ${err}`);
        callback(null, createResponse(500, err));
    });
}

exports.getitems = (event, context, callback) => {
    return simple_get(event, 'ITEMS_' + event.pathParameters.testId, callback)
};

exports.getresources = (event, context, callback) => {
    return simple_get(event, 'RESOURCES_' + event.pathParameters.testId, callback)
};