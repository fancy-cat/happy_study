import { Form, Radio,Button } from 'antd';
import React, { useState } from 'react';
import ToneFormItems from './toneFormItem';
import SentenceFormItem from './sentenceFormItem';
export default function Home() {
  const [form] = Form.useForm();
  const [type, setType] = useState(1);
  const typeOptions = [
    {
      label: '单词',
      value: 0
    },
    {
      label: '句子',
      value: 1
    },
    {
      label: '笔记',
      value: 2
    },
    {
      label: '疑问',
      value: 3
    },
  ];
  const onFinish = (values) => {
    console.log('Success:', values);
    // 调接口
  }
  const FormItems = ({formType}) => {
    return [<ToneFormItems />,<SentenceFormItem />][formType]
  }
  return <div>
     <Form
      form={form}
      style={{
        width: 400,
        maxWidth: 600,
      }}
      colon={false}
      initialValues={{
        type: 1
      }}
      onFinish={onFinish}
    >
      <Form.Item name="type">
        <Radio.Group
          optionType="button"
          value={type} 
          options={typeOptions}
          onChange={e => setType(e.target.value)}
        />
      </Form.Item>
      <FormItems formType={type} />
      <Form.Item>
        <Button type="primary" htmlType="submit">提交</Button>
      </Form.Item>
    </Form>
  </div>
}