import { App, CfnOutput, RemovalPolicy, Stack } from 'aws-cdk-lib'

interface IotProps {
  name: string
}

export class IotStack extends Stack {
  constructor(app: App, id: string, props: IotProps) {
    super(app, id)

  }
}