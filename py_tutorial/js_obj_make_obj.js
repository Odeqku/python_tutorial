#!/usr/bin/node

const salva = require ('./js_obj_constructor').createPerson;
const salva1 = salva('Salva', 25);
salva1.introduceSelf();


const frankie = require ('./js_obj_constructor').createPerson;
const frankie1 = frankie('Frankie', 30);
frankie1.introduceSelf();


const sammie = require ('./js_obj_constructor1').createPersons;
const sammie1 = sammie('Sammie');
sammie1.introduceSelf();
