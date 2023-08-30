import { App } from 'aws-cdk-lib'

import { S3Stack } from './stacks/s3-stack'
import { DynamoStack } from './stacks/dynamo-stack'
import { IotStack } from './stacks/iot-stack'

const PROJECT_NAME = 'propertyshield'

const app = new App()

const s3Stack = new S3Stack(app, `${PROJECT_NAME}-S3Stack`, { name: PROJECT_NAME })
const dynamoStack = new DynamoStack(app, `${PROJECT_NAME}-DynamoStack`, { name: PROJECT_NAME })

const iotStack = new IotStack(app, `${PROJECT_NAME}-IotStack`, { name: PROJECT_NAME })
iotStack.addDependency(dynamoStack)
iotStack.addDependency(s3Stack)

app.synth()